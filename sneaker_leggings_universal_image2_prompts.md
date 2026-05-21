# GPT-Image-2 球鞋与紧身裤穿搭通用修图提示词

## 参考来源

参考模板库：`E:\VISUAL_code\image-2\awesome-gpt-image-2-prompts-main\README.md`

主要借鉴：

- `Case 146: Streetwear Sneaker Poster Ad`：低机位、球鞋前景、街头海报。
- `Case 70: Luxury Sportswear Basketball Athlete Campaign Poster`：高级运动品牌广告。
- `Case 71: Streetwear Fashion Campaign Asian Apparel Poster`：现代街头穿搭 campaign。
- `Case 89: Luxury Studio Outfit Transformation`：保留原主体，改成棚拍。
- `Case 105: Black-and-red streetwear campaign portrait`：高反差图形化运动海报。
- `Case 168: Outdoor Sportswear Grid Campaign`：多图运动 campaign 结构。

## 通用底层约束

每次修图建议先放这段：

```text
Use the uploaded image as the reference photo. Preserve the same outfit identity: the same sneakers, socks, grey leggings / fitted athletic pants, visible sportswear details, pose direction, and natural body proportions. Keep the original casual sneaker-and-leggings styling, but improve the image into a polished sportswear / streetwear editorial photo. Do not change the shoe design, sock logo, clothing color, or overall outfit combination unless explicitly requested.
```

负面约束：

```text
Negative prompts: no extra limbs, no distorted feet, no warped shoes, no changed sneaker design, no fake logos, no unreadable random text, no body reshaping, no plastic skin, no over-smoothing, no cartoon, no anime, no watermark, no low-resolution artifacts, no messy background.
```

## 通用提示词 1：高级运动穿搭写真

适合：保留原照片真实感，只把它修成更高级的运动品牌穿搭图。

```text
Use the uploaded image as the reference photo. Preserve the same sneakers, grey socks, grey fitted athletic leggings / tight sports pants, top or visible sportswear details, and the original casual seated pose direction. Transform the image into a premium sportswear editorial photograph.

Clean up the indoor background and replace it with a minimal warm-gray studio or clean gym-lifestyle setting. Keep the camera angle close to the original, with a low-angle or top-down intimate perspective focused on the sneaker, sock, and leggings combination. Improve the composition so the sneakers and lower-body outfit feel intentional and stylish, not accidental.

Lighting: soft cinematic side light, subtle rim light on the sneakers and socks, realistic shadows, controlled highlights on shoe leather / synthetic panels, crisp ribbed sock texture, detailed heather-grey fabric texture on the leggings. Color grade: modern neutral sportswear palette, grey, charcoal, off-white, muted blue-green accents, clean contrast.

Style: high-end athletic lifestyle campaign, photorealistic, 35mm or 50mm editorial photography, shallow depth of field, realistic fabric folds, premium but natural. No text, no added logos, no extra accessories.

Negative prompts: no extra limbs, no distorted feet, no warped shoes, no changed sneaker design, no fake logos, no random text, no body reshaping, no plastic skin, no cartoon, no watermark.
```

## 通用提示词 2：球鞋主视觉广告

适合：让鞋成为主角，画面更像球鞋广告、产品主视觉。

```text
Use the uploaded image as the reference photo. Preserve the exact sneaker shape, color, material panels, laces, socks, and grey leggings / fitted athletic pants. Create a premium sneaker-focused advertising image based on the original pose and perspective.

Make the sneakers the dominant foreground subject. Recompose the image with a dynamic low-angle or top-down fashion product perspective: one shoe closer to the camera, the other slightly behind, with the legs and leggings forming strong diagonal lines. Keep the shoes realistic and wearable, with sharp lace texture, clean stitching, glossy and matte material contrast, realistic creases, and natural sole detail.

Background: clean textured studio floor or muted athletic mat surface, simplified and refined. Add subtle abstract sportswear graphics only as texture: soft diagonal motion lines, faint tactical grid marks, and minimal paper-grain / concrete texture. Do not add readable fake brand text.

Lighting: commercial product photography, directional softbox from one side, crisp highlights on the shoe surface, realistic contact shadows under the sole, high clarity, premium neutral grey color grading.

Mood: modern streetwear sneaker campaign, athletic, clean, confident, close-up editorial. Photorealistic, ultra-detailed, high-resolution.

Negative prompts: no changed shoe model, no extra shoes, no distorted laces, no fake logos, no unreadable text, no warped legs, no cartoon, no watermark.
```

## 通用提示词 3：街头海报 / 潮流拼贴版

适合：借鉴 `Case 146`，做更酷、更适合发社媒的街头海报。

```text
Use the uploaded image as the subject reference. Preserve the same sneakers, socks, grey leggings / athletic pants, and casual seated lower-body pose. Turn the image into a bold streetwear sneaker poster while keeping the outfit realistic.

Composition: vertical 4:5 or 9:16 poster. Place the sneakers and socks in the lower foreground as the main visual anchor, with the legs creating diagonal movement through the frame. Keep the person cropped naturally, emphasizing the sneaker-and-leggings styling rather than a full-body portrait.

Design style: off-white or charcoal textured paper background, subtle blue-green accents inspired by the original floor colors, restrained collage layers, torn paper edges, thin motion lines, light ink splatter, and abstract sports diagram marks. Use no readable text unless explicitly requested; graphic elements should feel like a premium streetwear campaign, not a busy poster.

Lighting and finish: high-contrast editorial flash mixed with soft studio fill, crisp fabric texture, detailed sock ribbing, realistic shoe creases, clean shadows, slightly gritty film grain, modern streetwear color grade.

Overall: urban sneaker culture, athletic fashion, premium sportswear poster, photorealistic, high resolution.

Negative prompts: no fake brand slogans, no random typography, no changed shoe design, no extra limbs, no distorted feet, no anime, no watermark.
```

## 通用提示词 4：保守清理增强版

适合：只想把照片修干净，不想大改。

```text
Enhance the uploaded image while keeping the original composition, outfit, and camera angle. Preserve the same sneakers, socks, grey leggings / fitted athletic pants, pose, and all visible clothing details.

Clean up noise and compression artifacts, improve sharpness, correct white balance, reduce harsh indoor lighting, recover detail in the shoes and socks, make the grey leggings texture clearer, and slightly improve contrast and color grading. Keep the floor / mat pattern recognizable but cleaner and less distracting.

Make the final result look like a well-edited smartphone sportswear outfit photo: natural, realistic, crisp, clean, and stylish. Do not add new objects, text, logos, people, or background changes.

Negative prompts: no identity change, no body reshaping, no changed shoe design, no fake logo, no extra limbs, no distorted laces, no over-smoothing, no artificial studio look, no watermark.
```

## 推荐使用顺序

1. 先用 `通用提示词 4` 测保真度。
2. 想要更高级但不夸张，用 `通用提示词 1`。
3. 想突出鞋，用 `通用提示词 2`。
4. 想做社媒海报，用 `通用提示词 3`。

