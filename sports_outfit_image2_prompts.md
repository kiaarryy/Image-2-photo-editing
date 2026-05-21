# GPT-Image-2 运动穿搭修图提示词

## 1. 当前图片判断

图片目录：`E:\VISUAL_code\image-2\image`

当前 4 张图的共同特点：

- 主体：白色足球球衣、白色运动袜、运动短裤、室内自拍低机位。
- 适合方向：足球穿搭写真、球衣街头海报、运动品牌感棚拍、低机位球鞋/袜子特写、社媒头像/封面图。
- 主要问题：构图太近，背景杂乱，球鞋没有成为明确主角，光线偏室内直白，画面缺少商业摄影的层次。

建议不要让模型大幅改人物身份和球衣图案。优先让它做：重新构图、换背景、增强光线、清理环境、强化球衣和袜鞋质感。

## 2. 参考模板来源

来自 `E:\VISUAL_code\image-2\awesome-gpt-image-2-prompts-main\README.md`，最适合复用的案例：

- `Case 146: Streetwear Sneaker Poster Ad`
  - 适合低机位、球鞋主角、街头海报、涂鸦拼贴。
- `Case 70: Luxury Sportswear Basketball Athlete Campaign Poster`
  - 适合把普通运动自拍改成高级运动广告大片。
- `Case 73 / Case 74: Avant-Garde Sports Fashion Ad`
  - 适合做更夸张的运动时尚海报，加入球、雕塑感、强视觉中心。
- `Case 89: Luxury Studio Outfit Transformation`
  - 适合保留原人物和衣服特征，改成干净棚拍。
- `Case 105: Black-and-red streetwear campaign portrait`
  - 适合黑白红高反差运动海报，和皇马白球衣很搭。
- `Case 52: 6-Block Fashion Campaign Prompt Formula`
  - 公式很实用：人物 + 穿搭 + 质感 + 场景 + 光线 + 镜头。
- `Case 168: Outdoor Sportswear Grid Campaign`
  - 适合做 2x2 多图运动穿搭 campaign，而不是单张修图。

## 3. 通用修图底层提示词

适合每张图都加在开头：

```text
Use the uploaded image as the reference photo. Preserve the same person, body proportions, pose direction, visible jersey design, socks, shorts, and overall outfit identity. Do not change the face identity if visible. Do not invent new logos or alter existing jersey crest and sponsor text. Improve the image into a high-end sports fashion editorial photograph. Clean up the background, improve composition, lighting, sharpness, fabric texture, and color grading while keeping the result photorealistic.
```

负面约束：

```text
No extra limbs, no distorted hands, no warped legs, no fake unreadable logos, no changed jersey crest, no plastic skin, no over-smoothing, no cartoon, no anime, no watermark, no random text, no messy background, no low-resolution artifacts.
```

## 4. 你的专属提示词模板

### A. 皇马球衣高级运动写真

用途：最稳，适合先测试。

```text
Use the uploaded image as the reference photo. Preserve the same person, pose, white Real Madrid-style football jersey, white socks, shorts, and visible outfit details. Transform the casual indoor selfie into a premium football fashion editorial photograph.

Recompose the image into a clean vertical 9:16 sports portrait with the subject seated in a relaxed low-angle pose. Keep the jersey as the visual focus, with crisp fabric weave, realistic folds, clean white highlights, and subtle shadows. Replace the cluttered indoor background with a minimal warm-gray studio wall and a slightly reflective floor. Add soft cinematic side lighting, gentle rim light on the shoulders and socks, realistic skin texture, and a polished magazine campaign color grade.

Mood: confident, clean, athletic, understated luxury football style. Photorealistic, high-resolution, editorial sportswear photography, 50mm lens look, shallow depth of field.

Negative: no extra limbs, no changed jersey crest, no fake text, no distorted socks, no warped legs, no plastic skin, no cartoon, no watermark.
```

### B. 低机位球鞋/袜子街头海报

用途：借鉴 `Case 146`。如果你想突出鞋、袜、腿部线条和运动穿搭，用这个。

```text
Use the uploaded image as the reference photo. Preserve the same person and outfit identity: white football jersey, white socks, athletic shorts, sporty styling. Create a bold streetwear sneaker poster advertisement from the original low-angle selfie.

Reframe the subject sitting casually on the ground with one knee closer to the camera and the sneaker / white sock area visually dominant in the foreground. Keep the body proportions natural. Make the jersey and socks sharp and tactile, with realistic cotton ribbing and football jersey mesh texture.

Background: off-white textured paper with subtle black and silver graphic accents inspired by football tactics boards, diagonal motion lines, light ink splatter, and torn paper collage. Use a restrained black / white / silver palette with one deep navy accent. Add only minimal abstract typography shapes, not readable fake brand text.

Lighting: high-contrast editorial flash mixed with soft studio fill, clean shadows, crisp highlights on white fabric. Overall style: urban football streetwear, youthful, premium, high-fashion sports poster, photorealistic.

Negative: no random brand logos, no unreadable text, no extra limbs, no distorted shoes, no changed jersey crest, no cartoon, no watermark.
```

### C. 黑白红运动广告海报

用途：借鉴 `Case 105`。适合做强视觉封面、头像背景、社媒海报。

```text
Use the uploaded image as the base. Preserve the same person, football jersey, socks, shorts, and pose direction. Convert the photo into a premium black-white-red sportswear campaign poster.

Make the subject high-contrast black and white, with the white jersey bright and detailed. Add controlled red graphic elements: one thin red horizontal bar, subtle geometric framing lines, a few angular motion shapes, and small football-field tactical marks. Keep the layout clean and premium, not cluttered.

Background: minimal textured charcoal-gray studio backdrop. Lighting: dramatic side light, sharp shadows, crisp fabric texture, realistic skin detail. Composition: vertical 4:5 or 9:16, subject centered slightly low, enough negative space at the top.

Do not add fake brand slogans or fake sponsor text. If typography is needed, use only abstract red blocks and lines without readable words.

Negative: no extra limbs, no face distortion, no changed jersey logo, no random text, no watermark, no anime, no over-smoothing.
```

### D. 足球场边 / 更真实的运动氛围

用途：把室内自拍变成像在训练场、球场边拍的照片。

```text
Use the uploaded image as the reference. Keep the same person, white football jersey, white socks, shorts, and relaxed seated pose. Transform the setting into a realistic football pitch sideline photoshoot at golden hour.

The subject sits near the edge of a clean green football field, with blurred stadium seats and soft field lights in the background. Keep the camera low and intimate, similar to the original selfie angle, but improve framing so the outfit reads clearly. The white jersey should look premium and authentic, with visible mesh texture, realistic wrinkles, and clean highlights.

Lighting: warm golden-hour side light, subtle rim light, soft cinematic shadows, natural skin texture. Lens: 35mm editorial sports photography, shallow depth of field, realistic bokeh. Mood: calm, confident, post-training football lifestyle.

Negative: no extra players, no crowd chaos, no fake logos, no changed crest, no random text, no plastic skin, no distorted limbs.
```

### E. 2x2 运动穿搭 Campaign

用途：借鉴 `Case 168`，一次生成四格风格图，适合做小红书/朋友圈组图封面。

```text
Use the uploaded image as the subject reference. Create a dynamic 2x2 grid collage of modern football sportswear lifestyle posters. Keep the same person and the same white football jersey / white socks / athletic shorts identity across all four panels.

Panel 1: clean studio sports portrait, seated low-angle pose, white jersey sharply lit, minimal gray background.
Panel 2: football pitch sideline at golden hour, relaxed post-training mood, blurred stadium background.
Panel 3: streetwear sneaker-and-socks close-up, low-angle composition, textured paper background with subtle football tactic graphics.
Panel 4: black-white-red campaign portrait, dramatic shadows, premium sports poster energy.

Use consistent identity, realistic body proportions, accurate outfit details, and polished editorial color grading. Add subtle graphic design elements only; avoid readable fake text. Photorealistic, high-resolution, premium football fashion campaign.

Negative: no extra limbs, no inconsistent identity, no changed jersey crest, no random text, no fake logos, no cartoon, no watermark.
```

### F. 保守型清理增强

用途：如果你只想修得更好看，不想大改。

```text
Enhance the uploaded image while keeping the original composition and outfit. Preserve the same person, pose, jersey, socks, shorts, and all visible clothing details. Clean the background slightly, reduce noise, improve sharpness, correct white balance, recover details in the white jersey and socks, smooth harsh indoor lighting, and add a subtle editorial sportswear color grade.

Keep the result natural and realistic, like a well-edited smartphone fashion photo. Do not change the camera angle dramatically. Do not add new objects, text, logos, or people.

Negative: no identity change, no body reshaping, no extra limbs, no changed jersey crest, no fake text, no over-smoothing, no artificial studio look.
```

## 5. 推荐使用顺序

1. 先用 `F. 保守型清理增强` 测模型是否能稳定保留球衣和身体结构。
2. 再用 `A. 皇马球衣高级运动写真` 做主图。
3. 如果想要更酷的海报感，用 `B` 或 `C`。
4. 如果想要一组内容，用 `E`。

## 6. 针对每张图的建议

- `图片_20260418230416_422_415.jpg`
  - 更适合 `B`：低机位、袜子和腿部前景强，可以做球鞋/袜子街头海报。
- `图片_20260418230922_423_415.jpg`
  - 更适合 `A` 或 `D`：坐姿和球衣较完整，可做运动写真。
- `图片_20260418230923_424_415.jpg`
  - 更适合 `A`：球衣 logo 区域清楚，适合高级球衣穿搭照。
- `图片_20260418230924_425_415.jpg`
  - 更适合 `C`：构图张力强，适合黑白红运动海报。

