# YouTube Image Animation (AI/CGI) Production & Upload SOP

Yeh standard operating procedure (SOP) images ko generate karne, unme realistic/cinematic movement dalne, audio-sync karne aur YouTube par publish karne ka complete framework provide karta hai.

---

## 1. Complete Workflow Architecture

```
Script & Scene Breakdown
       │
       ▼
Voiceover Generation / Audio Record
       │
       ▼
Base Image Generation (Text-to-Image)
       │
       ▼
Image-to-Video Animation (Motion Control)
       │
       ▼
Timeline Assembly & Sound Design (SFX/BGM)
       │
       ▼
Packaging (CTR Thumbnail + Title)
       │
       ▼
Staging (Unlisted) ➔ Scheduled Release
```

---

## 2. Step-by-Step Production SOP

### Step 1: Scripting & Scene Breakdown
- **Pacing Rule:** Har 3 se 5 seconds me visual change hona zaroori hai.
- **Scene Sheet Template:**
  | Scene # | Voiceover Segment (Dialogue) | Visual Description | Camera Motion Prompt | Duration |
  |---|---|---|---|---|
  | 01 | "Pichhle 100 saalon me yeh sheher badal chuka tha..." | Ruined futuristic city skyline, rain, neon lights | Drone shot slowly flying backward, heavy rain | 4 sec |
  | 02 | "Lekin underground bunker me koi zinda tha." | Young scientist looking at holographic screen | Medium close-up, screen flicker, eyes moving | 3.5 sec |

### Step 2: Voiceover (Pehla Audio Lock)
- Hamesha animation se **pehle** voiceover finalize karein taaki aapko pata ho har scene kitne second ka chahiye.
- **Audio Standards:**
  - Format: WAV (24-bit, 48kHz)
  - Loudness: Dialogue level $-14\text{ LUFS}$ target
  - Background noise: De-noised aur clean gate

### Step 3: Base Image Generation (Text-to-Image)
- **Aspect Ratio Settings:**
  - YouTube Long Form: `--ar 16:9`
  - YouTube Shorts: `--ar 9:16`
- **Character & Style Consistency:**
  - Style lock ke liye har prompt me ek fixed keyword group rakhein:
    > `cinematic lighting, hyper-realistic, photorealistic textures, 35mm lens, depth of field, Rec.709 color grading --v 6.1 --ar 16:9`
  - Multiple scenes me same character dikhane ke liye Character Reference tag (`--cref`) ya consistent face seed use karein.

### Step 4: Image-to-Video Animation (Motion Prompting)
Base image ko image-to-video tools me convert karte waqt distortion se bachne ke rules:

1. **Motion Prompting Formula:**
   ```
   [Subject Action] + [Camera Direction] + [Environmental Dynamics]
   ```
   * *Example:* "Young man turns his head toward the window, slow smooth camera dolly-in, soft wind rustling curtains, cinematic depth of field."

2. **Camera Controls:**
   - **Pan Left/Right:** Wide landscape ya tracking shot ke liye.
   - **Zoom/Dolly In:** Suspense, dramatic dialogue ya emotional moments ke liye.
   - **Tilt Up:** Kisi badi building ya monster ko reveal karne ke liye.
3. **Motion Intensity:** Slider ko `3 to 5` (medium) par rakhein. High intensity visual artifacts ya unnatural warping generate karti hai.

### Step 5: Timeline Assembly & Sound Design
Video editor (CapCut, Premiere Pro, DaVinci Resolve) me clips organize karein:

1. **Pacing & Cuts:**
   - Voiceover ke cadence ke saath cuts match karein.
   - Agar AI clip 4 seconds ki hai aur dialogue 6 seconds ka hai, toh clip par $10\text{--}15\%$ smooth optical flow slow-motion lagayein ya ek close-up cutaway add karein.
2. **Layered Sound Effects (Foley):**
   - AI visuals bina authentic sound ke lifeless lagte hain.
   - **SFX Stack:**
     - Layer 1: Ambient room/weather tone (rain, wind, machine hum)
     - Layer 2: Movement action (footsteps, cloth rustle, door creak)
     - Layer 3: Impact/Transition (subtle whoosh, riser, hit)
3. **Music:**
   - Background music track dialogue ke peeche $-22\text{ dB}$ se $-25\text{ dB}$ par set karein.

### Step 6: Visual Polish & Color Uniformity
Alag-alag AI clips ke color palette ko match karne ke liye:
- Timeline ke top par ek **Adjustment Layer** lagayein.
- Light film grain ($3\text{--}5\%$) aur subtle contrast LUT apply karein taaki sari clips ek single cinema camera se shoot hui lagein.

### Step 7: Export Specifications
- **Container:** MP4
- **Codec:** H.264 (Standard) ya H.265 / HEVC
- **Resolution:** $1920 \times 1080$ (FHD) ya $3840 \times 2160$ (4K)
- **Frame Rate:** $24\text{ fps}$ (Cinematic feel) ya $30\text{ fps}$
- **Bitrate:** Variable Bitrate (VBR, 2-pass), Target: $20\text{--}35\text{ Mbps}$ for 1080p, $50\text{--}70\text{ Mbps}$ for 4K.

---

## 3. Upload & YouTube Studio Configuration

1. **Upload Status:** Hamesha **Unlisted** mode me upload karein.
   - High-resolution (1080p/4K) processing complete hone me 20–45 minutes lagte hain.
2. **Thumbnail Packaging:**
   - AI se alag se ultra-clear $1280 \times 720$ thumbnail frame generate karein.
   - Face par clear emotion + 3 words ka punchy title text add karein.
3. **Metadata & Chapters:**
   - Description me timecodes dalein:
     ```
     00:00 - Introduction
     01:15 - The Awakening
     03:40 - The Discovery
     06:20 - Final Confrontation
     ```
4. **Schedule:** Peak time (India: Shaam 4:00 PM - 6:00 PM IST) par automatic release set karein.

---

## 4. Pre-Render & Pre-Upload Checklist

- [ ] Har scene ka aspect ratio 16:9 uniform hai (no black bars/letterboxing issues)
- [ ] Motion distortion ya warped limbs/faces trim kiye gaye hain
- [ ] Dialogue level $-14\text{ LUFS}$ calibrated hai
- [ ] Background music dialogue ko overpower nahi kar rahi
- [ ] Ambient SFX har visual movement ke saath synced hai
- [ ] Thumbnail mobile zoom level par clearly readable hai
- [ ] YouTube checks tab me green checkmark (No copyright flags) confirmed hai
