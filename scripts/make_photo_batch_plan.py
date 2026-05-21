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

DEFAULT_STYLE_ARCHETYPES = {
    "clean": "creator-clean-retouch",
    "travel_lifestyle": "warm-travel-editorial",
    "cinematic_portrait": "cinematic-social-portrait",
    "sports_action": "sports-editorial-action",
    "sportswear_fit": "streetwear-sports-fit",
    "sneaker_product": "commercial-sneaker-hero",
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
    parser.add_argument(
        "--target",
        default=None,
        help="Optional single image filename or relative path to include from the input folder.",
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
        "visual_summary",
        "category",
        "selected_skill",
        "style_archetype",
        "edit_intensity",
        "preserve",
        "aspect_ratio",
        "output_goal",
        "prompt_file",
        "output_file",
        "prompt_status",
        "qa_status",
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
                    "visual_summary": "",
                    "category": "",
                    "selected_skill": "",
                    "style_archetype": "",
                    "edit_intensity": "medium",
                    "preserve": "identity/outfit/shoes/logos/body-proportions",
                    "aspect_ratio": "4:5 or 9:16",
                    "output_goal": "",
                    "prompt_file": "",
                    "output_file": "",
                    "prompt_status": "todo",
                    "qa_status": "todo",
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
Prompts folder: `{manifest_path.parent / "prompts"}`
Edited outputs folder: `{manifest_path.parent / "edited"}`

## Fill Manifest

For agent-driven runs, inspect each image visually, then fill `visual_summary`, `category`, `selected_skill`, `style_archetype`, `output_goal`, `prompt_file`, and `output_file`.

{category_lines}

## Default Style Archetypes

{chr(10).join(f"- `{category}` -> `{style}`" for category, style in DEFAULT_STYLE_ARCHETYPES.items())}

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
- [ ] Final accepted files were copied into the run's `edited/` folder.
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
    if args.target:
        target = args.target.replace("\\", "/")
        images = [
            image
            for image in images
            if image.name == args.target or str(image.relative_to(input_dir)).replace("\\", "/") == target
        ]
        if not images:
            raise SystemExit(f"Target image not found under {input_dir}: {args.target}")
    manifest_path = output_dir / "manifest.csv"
    plan_path = output_dir / "batch_plan.md"
    (output_dir / "prompts").mkdir(exist_ok=True)
    (output_dir / "edited").mkdir(exist_ok=True)
    write_manifest(manifest_path, input_dir, images)
    write_plan(plan_path, input_dir, manifest_path, images)

    print(f"Images found: {len(images)}")
    print(f"Manifest: {manifest_path}")
    print(f"Plan: {plan_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
