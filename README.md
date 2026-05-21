# Image-2 Photo Editing

Agent-driven AI photo editing framework for mixed personal photo sets: travel/lifestyle portraits, cinematic social portraits, sports action, sportswear outfits, sneakers, and product/still-life images.

## What Is Included

- `skills/`: project-local Codex skills for automated routing, creator-inspired style selection, and style-specific retouching.
- `docs/photo-editing-skill-framework.md`: operating workflow and category map.
- `scripts/make_photo_batch_plan.py`: non-destructive run/manifest generator.
- `scripts/copy_generated_image_to_run.py`: copies generated images from Codex's temporary cache into the project run output.
- `AGENT.md`: project agent workflow guide.
- `sports_outfit_image2_prompts.md` and `sneaker_leggings_universal_image2_prompts.md`: earlier prompt references retained for compatibility.

## What Is Not Committed

- `image/`: local source photos.
- `outputs/`: generated manifests, plans, and edited outputs.
- `awesome-gpt-image-2-prompts-main/`: external downloaded prompt corpus and image assets.
- `.claude/`: local agent settings.

## Default Workflow

1. Put source photos in:

```text
E:\VISUAL_code\image-2\image
```

2. Ask Codex to run the `auto-photo-editing-pipeline` skill.

The agent should inspect each image, classify it, select a style archetype, generate the edit, copy the accepted image into the project output folder, and report the project path.

3. For manual run setup:

```powershell
python E:\VISUAL_code\image-2\scripts\make_photo_batch_plan.py --input E:\VISUAL_code\image-2\image
```

For one file:

```powershell
python E:\VISUAL_code\image-2\scripts\make_photo_batch_plan.py --input E:\VISUAL_code\image-2\image --target IMG_001.jpg
```

4. Final edited files are saved under:

```text
E:\VISUAL_code\image-2\outputs\photo_editing_batch\<run-id>\edited
```

Codex's default generated-image folder is treated as temporary cache only.

## Skill Routes

- `auto-photo-editing-pipeline`: end-to-end intake, classification, style selection, editing, project output copy, and QA.
- `photo-editing-batch-router`: classify mixed batches and assemble prompts.
- `photo-clean-retouch`: conservative cleanup and quality improvement.
- `travel-lifestyle-portrait-editor`: travel, daily-life, cafe, street, hotel, and vacation portraits.
- `cinematic-social-portrait-editor`: moody city, night, and social-feed portraits.
- `sports-action-editor`: indoor/outdoor sports and athletic movement photos.
- `sportswear-fit-editor`: jersey, leggings, socks, gym fit, and sport-fashion images.
- `sneaker-product-editor`: sneakers, shoes, accessories, and still-life product photos.

## Style Archetypes

The project does not copy a living creator exactly. It translates public creator/tutorial patterns into reusable archetypes such as `warm-travel-editorial`, `cinematic-social-portrait`, `streetwear-sports-fit`, `commercial-sneaker-hero`, and `dynamic-product-campaign`.
