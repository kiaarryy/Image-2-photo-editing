---
name: photo-editing-batch-router
description: Use when planning or running batch AI image editing for mixed travel, lifestyle portrait, sports, sportswear outfit, sneaker, product, or social-media photo sets.
---

# Photo Editing Batch Router

## Core Rule

Route by photo intent first, then by social-media style archetype. Creator/blogger references are grounding signals only; write concrete photographic instructions and never ask for an exact living-person style clone.

For full drop-folder execution, use `auto-photo-editing-pipeline` first. This router owns classification and prompt assembly logic.

## Batch Workflow

1. Inventory the input folder and create a manifest with: `file`, `visual_summary`, `category`, `selected_skill`, `style_archetype`, `preserve`, `aspect_ratio`, `output_goal`, `prompt_file`, `output_file`, `prompt_status`, `qa_status`.
2. Classify each image into one primary route:
   - `photo-clean-retouch`: keep original composition, clean and improve.
   - `travel-lifestyle-portrait-editor`: travel, daily life, cafe, street, hotel, architecture, vacation portraits.
   - `cinematic-social-portrait-editor`: city portrait, night street, moody feed image, profile cover, expressive social portrait.
   - `sports-action-editor`: gym, running, ball sports, court/field, action, sweat, motion.
   - `sportswear-fit-editor`: athletic outfit, leggings, jersey, socks, full-body or mirror/selfie fashion.
   - `sneaker-product-editor`: shoes, sneakers, product close-up, e-commerce or campaign hero.
3. For each style group, process 3-8 images first as a calibration wave. Do not apply a strong look to the whole batch until the identity, outfit, shoe shape, and color grade are stable.
4. Reuse one consistent base constraint across the batch:

```text
Use the uploaded image as the reference photo. Preserve the same person identity if visible, natural body proportions, pose direction, outfit identity, shoe design, logos/crests/text that already exist, and the original photo's believable physical structure. Improve lighting, composition, background cleanliness, color grade, texture, sharpness, and editorial finish while keeping the result photorealistic.
```

5. Add a creator/social-media style archetype from `../auto-photo-editing-pipeline/references/style-archetypes.md`.
6. Add route-specific prompt blocks from the selected skill.
7. Add negatives for every image:

```text
No extra limbs, no distorted hands or feet, no warped shoes, no changed logos or jersey crests, no fake unreadable text, no plastic skin, no over-smoothing, no cartoon, no anime, no watermark, no low-resolution artifacts.
```

## Decision Table

| If the image mainly shows | Choose | Output target |
|---|---|---|
| A good photo that only needs cleanup | `photo-clean-retouch` | Natural polished image |
| Travel/daily portrait with place atmosphere | `travel-lifestyle-portrait-editor` | Warm editorial lifestyle |
| Street/city/night portrait or social cover | `cinematic-social-portrait-editor` | Moody cinematic feed image |
| Body in motion or sport venue | `sports-action-editor` | Dynamic sports editorial |
| Outfit, jersey, leggings, socks, gym fit | `sportswear-fit-editor` | Athletic fashion campaign |
| Sneakers/product detail | `sneaker-product-editor` | Commercial product hero |

## Style Archetype Table

| Desired social-media look | style_archetype |
|---|---|
| Natural polished cleanup | `creator-clean-retouch` |
| Warm travel/lifestyle | `warm-travel-editorial` |
| Cinematic city/social portrait | `cinematic-social-portrait` |
| Fashion portrait retouch | `fashion-portrait-retouch` |
| Sport action editorial | `sports-editorial-action` |
| Sport outfit / streetwear fit | `streetwear-sports-fit` |
| Sneaker product hero | `commercial-sneaker-hero` |
| Graphic product campaign | `dynamic-product-campaign` |

## Quality Gate

Before accepting a batch, check:

- Identity and body proportions are stable across images.
- Shoes, socks, jersey crests, clothing colors, and existing logos did not drift.
- Whites keep texture; blacks do not crush important details.
- Background cleanup does not invent unreadable signage.
- The look is consistent inside each style group, not across all categories.
- Final accepted outputs are copied into the project run `edited/` folder.

Read `references/creator-source-notes.md` only when source grounding or style rationale is needed.
