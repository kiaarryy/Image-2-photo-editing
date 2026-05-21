# Image-2 Photo Editing

Batch-oriented AI photo editing framework for mixed personal photo sets: travel/lifestyle portraits, cinematic social portraits, sports action, sportswear outfits, sneakers, and product/still-life images.

## What Is Included

- `skills/`: project-local Codex skills for routing and style-specific retouching.
- `docs/photo-editing-skill-framework.md`: operating workflow and category map.
- `scripts/make_photo_batch_plan.py`: non-destructive manifest generator for batch planning.
- `AGENT.md`: project agent workflow guide.
- `sports_outfit_image2_prompts.md` and `sneaker_leggings_universal_image2_prompts.md`: earlier prompt references retained for compatibility.

## What Is Not Committed

- `image/`: local source photos.
- `outputs/`: generated manifests, plans, and edited outputs.
- `awesome-gpt-image-2-prompts-main/`: external downloaded prompt corpus and image assets.
- `.claude/`: local agent settings.

## Basic Workflow

Create a manifest for the current local image folder:

```powershell
python E:\VISUAL_code\image-2\scripts\make_photo_batch_plan.py --input E:\VISUAL_code\image-2\image
```

Then fill the generated `manifest.csv` with category, selected skill, output goal, and per-file notes. Start with a small calibration wave before processing the full batch.

## Skill Routes

- `photo-editing-batch-router`: classify mixed batches and assemble prompts.
- `photo-clean-retouch`: conservative cleanup and quality improvement.
- `travel-lifestyle-portrait-editor`: travel, daily-life, cafe, street, hotel, and vacation portraits.
- `cinematic-social-portrait-editor`: moody city, night, and social-feed portraits.
- `sports-action-editor`: indoor/outdoor sports and athletic movement photos.
- `sportswear-fit-editor`: jersey, leggings, socks, gym fit, and sport-fashion images.
- `sneaker-product-editor`: sneakers, shoes, accessories, and still-life product photos.

