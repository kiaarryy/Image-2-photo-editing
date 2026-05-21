---
name: auto-photo-editing-pipeline
description: Use when the user wants images dropped into image-2/image to be automatically classified, routed to a photo editing style, edited with GPT image generation, and saved into project outputs.
---

# Auto Photo Editing Pipeline

## Goal

Turn `E:\VISUAL_code\image-2\image` into the intake folder: inspect each source image, classify it visually, select a project skill and creator-inspired style archetype, generate an edited image, and save the accepted final under `E:\VISUAL_code\image-2\outputs`.

## Output Rule

Treat Codex's default generated-image folder as temporary cache only. After every `image_gen` edit, immediately copy the selected image into:

```text
E:\VISUAL_code\image-2\outputs\photo_editing_batch\<run-id>\edited\
```

Use:

```powershell
python E:\VISUAL_code\image-2\scripts\copy_generated_image_to_run.py --run-dir <run-dir> --name <source-stem>_<style>_edited.png
```

Do not delete the default cache. The project output path is the only final deliverable path to report.

## Automatic Workflow

1. Create a run:

```powershell
python E:\VISUAL_code\image-2\scripts\make_photo_batch_plan.py --input E:\VISUAL_code\image-2\image --run-id <run-id>
```

For one file, add `--target <filename>`.

2. For each row in `manifest.csv`, inspect the local image with `view_image`.
3. Fill these row fields from visual inspection:
   - `visual_summary`: one sentence describing subject, setting, and defects.
   - `category`: one of `clean`, `travel_lifestyle`, `cinematic_portrait`, `sports_action`, `sportswear_fit`, `sneaker_product`.
   - `selected_skill`: matching project skill.
   - `style_archetype`: pick one from `references/style-archetypes.md`.
   - `output_goal`: concrete result such as `commercial sneaker hero` or `warm travel lifestyle portrait`.
   - `prompt_file`: `prompts/<source-stem>_<style>.md`.
   - `output_file`: `edited/<source-stem>_<style>_edited.png`.
4. Read the selected skill plus `references/style-archetypes.md`.
5. Write a final prompt file in the run `prompts/` folder. The prompt must include:
   - preservation block
   - selected skill recipe
   - selected style archetype
   - file-specific visible details to preserve
   - negative prompt
6. Use built-in `image_gen` to edit the visible image.
7. Copy the generated image into the run `edited/` folder with `copy_generated_image_to_run.py`.
8. Open the project-copied output with `view_image` and QA it against the manifest.
9. Update `qa_status` to `pass`, `needs_retry`, or `rejected`.

## Classification Guide

| Visual signal | category | selected_skill |
|---|---|---|
| Only needs cleanup | `clean` | `photo-clean-retouch` |
| Person plus travel/place atmosphere | `travel_lifestyle` | `travel-lifestyle-portrait-editor` |
| City/night/social portrait | `cinematic_portrait` | `cinematic-social-portrait-editor` |
| Body in sport motion or sport venue | `sports_action` | `sports-action-editor` |
| Outfit, jersey, socks, leggings, gym fit | `sportswear_fit` | `sportswear-fit-editor` |
| Sneakers, shoes, accessories, product detail | `sneaker_product` | `sneaker-product-editor` |

## Style Rule

Use creator/social-media references as visual recipes, not exact imitation. Say "creator-inspired clean fashion editorial" or "moody street creator grade", not "in the exact style of [living person]".

Read `references/style-archetypes.md` when choosing the style.
