# Phase 10: Optional AI motion and AI model (extra, not core)

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 10a | Image-to-video adapter interface | Mock provider works | |
| 10b | One free model on Colab/Kaggle (for example Wan or LTX-Video), 3-5s clips | Clip generated from a product photo | Slow, session limits, GPU memory |
| 10c | Product integrity check: compare the clip's product against the original (SSIM or CLIP similarity) | Morphed logos or shapes rejected | Threshold tuning |
| 10d | Fallback to Phase 6 motion on rejection | User always gets a video | |
| 10e | AI human model holding or using the product | Test only after 10c works | Distorted hands, uncanny faces, and consent/likeness issues |

---

## Sub-phase details

### 10a

#### Build
Image-to-video adapter interface

#### Pass check
Mock provider works

#### Known issues
(none)

### 10b

#### Build
One free model on Colab/Kaggle (for example Wan or LTX-Video), 3-5s clips

#### Pass check
Clip generated from a product photo

#### Known issues
Slow, session limits, GPU memory

### 10c

#### Build
Product integrity check: compare the clip's product against the original (SSIM or CLIP similarity)

#### Pass check
Morphed logos or shapes rejected

#### Known issues
Threshold tuning

### 10d

#### Build
Fallback to Phase 6 motion on rejection

#### Pass check
User always gets a video

#### Known issues
(none)

### 10e

#### Build
AI human model holding or using the product

#### Pass check
Test only after 10c works

#### Known issues
Distorted hands, uncanny faces, and consent/likeness issues
