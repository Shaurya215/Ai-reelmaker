# Phase 6: Motion

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 6a | Slow zoom on a single scene | Smooth 5s clip | Jitter from zoompan rounding: scale up first, then zoom |
| 6b | Pan left/right and up/down | No edge showing | Pan beyond canvas |
| 6c | Parallax: product layer and background layer move at different speeds | Visible depth, no tearing | Edge gaps between layers |
| 6d | Multiple scenes with transitions (fade, slide) | 15s sequence joins smoothly | Audio-video length mismatch |
| 6e | Scene durations driven by the voiceover timing | Visuals change at the right words | Drift on long scripts |

---

## Sub-phase details

### 6a

#### Build
Slow zoom on a single scene

#### Pass check
Smooth 5s clip

#### Known issues
Jitter from zoompan rounding: scale up first, then zoom

### 6b

#### Build
Pan left/right and up/down

#### Pass check
No edge showing

#### Known issues
Pan beyond canvas

### 6c

#### Build
Parallax: product layer and background layer move at different speeds

#### Pass check
Visible depth, no tearing

#### Known issues
Edge gaps between layers

### 6d

#### Build
Multiple scenes with transitions (fade, slide)

#### Pass check
15s sequence joins smoothly

#### Known issues
Audio-video length mismatch

### 6e

#### Build
Scene durations driven by the voiceover timing

#### Pass check
Visuals change at the right words

#### Known issues
Drift on long scripts
