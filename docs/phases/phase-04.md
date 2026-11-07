# Phase 4: Product image prep

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 4a | Background removal (rembg) | Cutout produced for all 10 | Slow on CPU |
| 4b | Mask cleanup: edge smoothing, remove halo | Zoom to 300%, no white fringe | Hair, fabric, and fine edges |
| 4c | Crop to product bounds, add padding | Product centered, nothing clipped | Shadows included in the mask by mistake |
| 4d | Upscale low-res products (Real-ESRGAN or Lanczos) | No visible blur at 1080 wide | Upscaling can distort text on packaging |
| 4e | Support gate: detect or let the user flag unsupported types | Glass, transparent, and white-on-white get a clear "not supported yet" | Decide your launch scope here |
| 4f | Place cutout on a 1080×1920 transparent canvas | Product is a consistent size and position | Very wide or very tall products |

---

## Sub-phase details

### 4a

#### Build
Background removal (rembg)

#### Pass check
Cutout produced for all 10

#### Known issues
Slow on CPU

### 4b

#### Build
Mask cleanup: edge smoothing, remove halo

#### Pass check
Zoom to 300%, no white fringe

#### Known issues
Hair, fabric, and fine edges

### 4c

#### Build
Crop to product bounds, add padding

#### Pass check
Product centered, nothing clipped

#### Known issues
Shadows included in the mask by mistake

### 4d

#### Build
Upscale low-res products (Real-ESRGAN or Lanczos)

#### Pass check
No visible blur at 1080 wide

#### Known issues
Upscaling can distort text on packaging

### 4e

#### Build
Support gate: detect or let the user flag unsupported types

#### Pass check
Glass, transparent, and white-on-white get a clear "not supported yet"

#### Known issues
Decide your launch scope here

### 4f

#### Build
Place cutout on a 1080×1920 transparent canvas

#### Pass check
Product is a consistent size and position

#### Known issues
Very wide or very tall products
