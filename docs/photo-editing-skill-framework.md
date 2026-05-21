# Image-2 Batch Photo Editing Skill Framework

## Purpose

This project now uses a router plus focused style skills instead of one broad photographer-style skill. The goal is batchable, repeatable AI retouching for mixed photo sets: travel/lifestyle portraits, cinematic social portraits, indoor/outdoor sports, sportswear outfits, sneakers, and product/still-life images.

## Skill Map

| Need | Skill |
|---|---|
| Batch classification and workflow | `E:\VISUAL_code\image-2\skills\photo-editing-batch-router\SKILL.md` |
| Conservative cleanup | `E:\VISUAL_code\image-2\skills\photo-clean-retouch\SKILL.md` |
| Travel/lifestyle portraits | `E:\VISUAL_code\image-2\skills\travel-lifestyle-portrait-editor\SKILL.md` |
| Cinematic social portraits | `E:\VISUAL_code\image-2\skills\cinematic-social-portrait-editor\SKILL.md` |
| Indoor/outdoor sports action | `E:\VISUAL_code\image-2\skills\sports-action-editor\SKILL.md` |
| Sportswear, jersey, leggings, outfit photos | `E:\VISUAL_code\image-2\skills\sportswear-fit-editor\SKILL.md` |
| Sneakers, shoes, still-life products | `E:\VISUAL_code\image-2\skills\sneaker-product-editor\SKILL.md` |

## Operating Flow

1. Put source images under `E:\VISUAL_code\image-2\image` or pass another input folder.
2. Generate a batch plan:

```powershell
python E:\VISUAL_code\image-2\scripts\make_photo_batch_plan.py --input E:\VISUAL_code\image-2\image
```

3. Open the generated `manifest.csv` and fill `category`, `selected_skill`, `aspect_ratio`, and `output_goal` for each file.
4. For each style group, start with 3-8 calibration images before processing the whole batch.
5. Use the selected skill's prompt recipe and add any file-specific constraints.
6. Save outputs by run and style group, then QA against the router checklist.

## Category Defaults

| Category | Default Skill |
|---|---|
| `clean` | `photo-clean-retouch` |
| `travel_lifestyle` | `travel-lifestyle-portrait-editor` |
| `cinematic_portrait` | `cinematic-social-portrait-editor` |
| `sports_action` | `sports-action-editor` |
| `sportswear_fit` | `sportswear-fit-editor` |
| `sneaker_product` | `sneaker-product-editor` |

## Prompt Assembly Pattern

Use this order for each image:

1. Universal preservation block from `photo-editing-batch-router`.
2. One route-specific recipe from the selected skill.
3. File-specific notes, such as "keep Real Madrid-style jersey crest unchanged" or "shoe must stay the same colorway".
4. Universal negative prompt.

## Source Grounding

The source notes live at `E:\VISUAL_code\image-2\skills\photo-editing-batch-router\references\creator-source-notes.md`. They summarize browsed creator/tutorial signals from Mango Street, Jessica Kobeissi, Julia Trotti, Jordan Matter, Talru Sports Photography, PHLEARN, Fstoppers, and Lightroom color-grading references. They are intentionally converted into generic workflows and visual recipes, not exact creator mimicry.
