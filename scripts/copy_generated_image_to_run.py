#!/usr/bin/env python
"""Copy the latest Codex-generated image into a project run directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy a generated image from Codex's default cache into a project output run."
    )
    parser.add_argument(
        "--source",
        default=None,
        help="Optional exact generated image path. If omitted, the newest generated image is used.",
    )
    parser.add_argument(
        "--generated-root",
        default=str(Path.home() / ".codex" / "generated_images"),
        help="Generated image cache root. Defaults to the Codex generated_images folder.",
    )
    parser.add_argument(
        "--run-dir",
        required=True,
        help="Project run directory, for example outputs/photo_editing_batch/<run-id>.",
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Destination filename, for example IMG_001_edited.png.",
    )
    return parser.parse_args()


def newest_generated_image(root: Path) -> Path:
    candidates = [
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    ]
    if not candidates:
        raise SystemExit(f"No generated images found under {root}")
    return max(candidates, key=lambda path: path.stat().st_mtime)


def main() -> int:
    args = parse_args()
    source = Path(args.source) if args.source else newest_generated_image(Path(args.generated_root))
    if not source.exists() or not source.is_file():
        raise SystemExit(f"Generated image does not exist: {source}")

    run_dir = Path(args.run_dir)
    edited_dir = run_dir / "edited"
    edited_dir.mkdir(parents=True, exist_ok=True)
    destination = edited_dir / args.name
    shutil.copy2(source, destination)

    print(f"Source: {source}")
    print(f"Destination: {destination}")
    print(f"Bytes: {destination.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
