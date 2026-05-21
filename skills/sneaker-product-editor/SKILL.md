---
name: sneaker-product-editor
description: Use when editing sneaker, shoe, fashion accessory, still-life, product close-up, e-commerce, or product-campaign images.
---

# Sneaker Product Editor

## Visual Direction

Product-first commercial image: accurate shape, premium materials, clean lighting, controlled shadows, and a clear hero composition. Use this when sneakers or still-life objects are the main subject.

## Prompt Recipe

```text
Use the uploaded image as the exact product reference. Preserve the same sneaker or object shape, colorway, panels, stitching, laces, sole shape, logo placement if present, material finish, scale, and visible wear marks unless cleanup is explicitly requested. Create a premium commercial product photograph from the original image.

Make the product the visual anchor with a clean hero composition. Improve lighting using a large softbox feel, crisp edge highlights, realistic contact shadows, material separation between matte fabric, leather, rubber, mesh, metal, or plastic, and sharp but natural detail. Clean dust, stains, and background clutter only if it does not change the product identity.

Background options: neutral studio surface, textured concrete, athletic mat, off-white paper, or restrained streetwear campaign surface. Add subtle abstract motion lines, paper grain, or tactical marks only when the user asks for a campaign look. Do not add readable fake brand text.

Negative: no changed shoe model, no extra shoes, no distorted laces, no fake logo, no unreadable text, no melted sole, no warped perspective, no plastic-looking material, no cartoon, no watermark.
```

## Variants

- `ecommerce-clean`: white/gray background, accurate product, soft shadow.
- `campaign-hero`: dynamic crop, textured surface, stronger contrast.
- `worn-authentic`: keep creases and wear, clean only distracting dirt.
- `flatlay-still-life`: top-down composition, props only if already present or requested.

## QA

A successful edit can sell the same shoe/object. If the colorway, sole, lace structure, or logo placement changes, reject it.
