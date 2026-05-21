#!/usr/bin/env python
"""Create a non-destructive batch photo editing manifest and prompt plan."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".heic"}

CATEGORY_TO_SKILL = {
    "clean": "photo-clean-retouch",
    "travel_lifestyle": "travel-lifestyle-portrait-editor",
    "cinematic_portrait": "cinematic-social-portrait-editor",
    "sports_action": "sports-action-editor",
    "sportswear_fit": "sportswear-fit-editor",
    "sneaker_product": "sneaker-product-editor",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a batch retouching manifest for the image-2 photo editing skills."
    )
    parser.add_argument(
        "--input",
        default="image",
        help="Input image folder. Defaults to ./image.",
    )
    parser.add_argument(
        "--output-root",
        default="outputs/photo_editing_batch",
        help="Output root for generated manifests. Defaults to ./outputs/photo_editing_batch.",
    )
    parser.add_argument(
        "--run-id",
        default=None,
        help="Optional run id. Defaults to timestamp.",
    )
    return parser.parse_args()


def iter_images(input_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in input_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )


def write_manifest(manifest_path: Path, input_dir: Path, images: list[Path]) -> None:
    fields = [
        "file",
        "relative_path",
        "category",
        "selected_skill",
        "preserve",
        "aspect_ratio",
        "output_goal",
        "prompt_status",
        "notes",
    ]
    with manifest_path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for image in images:
            writer.writerow(
                {
                    "file": image.name,
                    "relative_path": str(image.relative_to(input_dir)),
                    "category": "",
                    "selected_skill": "",
                    "preserve": "identity/outfit/shoes/logos/body-proportions",
                    "aspect_ratio": "4:5 or 9:16",
                    "output_goal": "",
                    "prompt_status": "todo",
                    "notes": "",
                }
            )


def write_plan(plan_path: Path, input_dir: Path, manifest_path: Path, images: list[Path]) -> None:
    category_lines = "\n".join(
        f"- `{category}` -> `{skill}`" for category, skill in CATEGORY_TO_SKILL.items()
    )
    image_lines = "\n".join(f"- [ ] `{image.name}`" for image in images)
    plan_path.write_text(
        f"""# Photo Editing Batch Plan

Generated: {datetime.now().isoformat(timespec="seconds")}
Input folder: `{input_dir}`
Manifest: `{manifest_path}`

## Fill Manifest

Set `category`, `selected_skill`, `output_goal`, and any file-specific `notes`.

{category_lines}

## Universal Preservation Block

```text
Use the uploaded image as the reference photo. Preserve the same person identity if visible, natural body proportions, pose direction, outfit identity, shoe design, logos/crests/text that already exist, and the original photo's believable physical structure. Improve lighting, composition, background cleanliness, color grade, texture, sharpness, and editorial finish while keeping the result photorealistic.
```

## Universal Negative Prompt

```text
No extra limbs, no distorted hands or feet, no warped shoes, no changed logos or jersey crests, no fake unreadable text, no plastic skin, no over-smoothing, no cartoon, no anime, no watermark, no low-resolution artifacts.
```

## Images

{image_lines if image_lines else "- No images found."}

## QA Checklist

- [ ] Same person/outfit/shoe identity is preserved.
- [ ] Existing logos, jersey crests, and visible text did not drift.
- [ ] White clothing keeps texture and does not become flat.
- [ ] Hands, feet, legs, and shoe geometry are natural.
- [ ] Batch look is consistent within each selected skill group.
""",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    cwd = Path.cwd()
    input_dir = Path(args.input)
    if not input_dir.is_absolute():
        input_dir = cwd / input_dir
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = cwd / output_root

    if not input_dir.exists() or not input_dir.is_dir():
        raise SystemExit(f"Input folder does not exist: {input_dir}")

    run_id = args.run_id or datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = output_root / run_id
    output_dir.mkdir(parents=True, exist_ok=True)

    images = iter_images(input_dir)
    manifest_path = output_dir / "manifest.csv"
    plan_path = output_dir / "batch_plan.md"
    write_manifest(manifest_path, input_dir, images)
    write_plan(plan_path, input_dir, manifest_path, images)

    print(f"Images found: {len(images)}")
    print(f"Manifest: {manifest_path}")
    print(f"Plan: {plan_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
