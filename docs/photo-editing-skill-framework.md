# Image-2 Batch Photo Editing Skill Framework

## Purpose

This project now uses an automated pipeline, a router, creator-inspired style archetypes, and focused style skills instead of one broad photographer-style skill. The goal is batchable, repeatable AI retouching for mixed photo sets: travel/lifestyle portraits, cinematic social portraits, indoor/outdoor sports, sportswear outfits, sneakers, and product/still-life images.

## Skill Map

| Need | Skill |
|---|---|
| End-to-end drop-folder workflow | `E:\VISUAL_code\image-2\skills\auto-photo-editing-pipeline\SKILL.md` |
| Batch classification and workflow | `E:\VISUAL_code\image-2\skills\photo-editing-batch-router\SKILL.md` |
| Conservative cleanup | `E:\VISUAL_code\image-2\skills\photo-clean-retouch\SKILL.md` |
| Travel/lifestyle portraits | `E:\VISUAL_code\image-2\skills\travel-lifestyle-portrait-editor\SKILL.md` |
| Cinematic social portraits | `E:\VISUAL_code\image-2\skills\cinematic-social-portrait-editor\SKILL.md` |
| Indoor/outdoor sports action | `E:\VISUAL_code\image-2\skills\sports-action-editor\SKILL.md` |
| Sportswear, jersey, leggings, outfit photos | `E:\VISUAL_code\image-2\skills\sportswear-fit-editor\SKILL.md` |
| Sneakers, shoes, still-life products | `E:\VISUAL_code\image-2\skills\sneaker-product-editor\SKILL.md` |

## Operating Flow

1. Put source images under `E:\VISUAL_code\image-2\image`.
2. Ask Codex to use `auto-photo-editing-pipeline`.
3. The agent creates a run:

```powershell
python E:\VISUAL_code\image-2\scripts\make_photo_batch_plan.py --input E:\VISUAL_code\image-2\image --run-id <run-id>
```

For one file, add `--target <filename>`.

4. The agent visually inspects each image, fills `manifest.csv`, selects a style archetype, and writes a prompt file under `prompts/`.
5. The agent calls image generation/editing.
6. The agent immediately copies the generated result into the run `edited/` folder with:

```powershell
python E:\VISUAL_code\image-2\scripts\copy_generated_image_to_run.py --run-dir <run-dir> --name <source-stem>_<style>_edited.png
```

7. The agent opens the project-copied output, QA checks it, and updates/report paths.

## Category Defaults

| Category | Default Skill |
|---|---|
| `clean` | `photo-clean-retouch` |
| `travel_lifestyle` | `travel-lifestyle-portrait-editor` |
| `cinematic_portrait` | `cinematic-social-portrait-editor` |
| `sports_action` | `sports-action-editor` |
| `sportswear_fit` | `sportswear-fit-editor` |
| `sneaker_product` | `sneaker-product-editor` |

## Style Archetype Defaults

| Category | Default Style Archetype |
|---|---|
| `clean` | `creator-clean-retouch` |
| `travel_lifestyle` | `warm-travel-editorial` |
| `cinematic_portrait` | `cinematic-social-portrait` |
| `sports_action` | `sports-editorial-action` |
| `sportswear_fit` | `streetwear-sports-fit` |
| `sneaker_product` | `commercial-sneaker-hero` |

## Prompt Assembly Pattern

Use this order for each image:

1. Universal preservation block from `photo-editing-batch-router`.
2. One route-specific recipe from the selected skill.
3. One style archetype from `E:\VISUAL_code\image-2\skills\auto-photo-editing-pipeline\references\style-archetypes.md`.
4. File-specific visible details, such as "keep Real Madrid-style jersey crest unchanged" or "shoe must stay the same colorway".
5. Universal negative prompt.

## Source Grounding

The source notes live at `E:\VISUAL_code\image-2\skills\photo-editing-batch-router\references\creator-source-notes.md`. Style recipes live at `E:\VISUAL_code\image-2\skills\auto-photo-editing-pipeline\references\style-archetypes.md`. They are intentionally converted into generic workflows and visual recipes, not exact creator mimicry.
