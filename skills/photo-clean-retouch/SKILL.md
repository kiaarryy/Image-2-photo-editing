---
name: photo-clean-retouch
description: Use when an uploaded image should be improved conservatively without changing the subject, outfit, scene identity, pose, or composition.
---

# Photo Clean Retouch

## Use This For

Default first pass for any uncertain photo, or when the user asks for natural cleanup, better quality, less clutter, sharper detail, and improved color without a new concept.

## Prompt Recipe

```text
Enhance the uploaded image while keeping the original composition, camera angle, person identity if visible, pose, outfit, shoe design, object shape, and scene identity. Clean distracting clutter only when it does not alter the story of the photo. Correct white balance, recover highlight and shadow detail, improve sharpness, reduce noise and compression artifacts, make fabric/material texture clearer, and add a subtle professional editorial color grade.

Keep the result natural, realistic, and believable, like a carefully edited high-quality smartphone or mirrorless-camera photo. Do not add new objects, new people, text, logos, accessories, or artificial studio effects unless explicitly requested.

Negative: no identity change, no body reshaping, no changed outfit or shoe design, no fake logo, no random text, no extra limbs, no distorted hands or feet, no over-smoothed skin, no plastic texture, no cartoon, no watermark.
```

## Adjustment Priorities

- Preserve first: identity, pose, body proportions, outfit, shoes, logos, visible text, scene logic.
- Improve second: exposure, color cast, background cleanliness, local contrast, texture, grain/noise.
- Avoid: heavy beauty retouch, face reshaping, unreal bokeh, fake studio backgrounds, random typography.

## QA

Reject the result if the edited image looks like a different person, different shoe model, different jersey/clothing design, or an AI-generated replacement rather than a cleaned version.
