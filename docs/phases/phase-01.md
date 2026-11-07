# Phase 1: Input and validation

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 1a | Function that accepts an image path and copies it to `jobs/<id>/input` | File saved, job ID generated | Duplicate names, special characters |
| 1b | Convert HEIC/WebP/JPEG to PNG | All formats open and save correctly | HEIC needs `pillow-heif` |
| 1c | Fix EXIF rotation | Phone photos appear upright | Sideways photos |
| 1d | Quality checks: min 800px, blur score, max file size | Tiny and blurry photos rejected with a clear message | Blur threshold needs tuning on your set |
| 1e | Product details schema (name, price, features, target customer, language, tone) | Missing fields give a readable error | Users entering vague or very long text |
| 1f | Output a clean `product.json` | All 10 products produce valid JSON, bad ones fail cleanly | Non-English text encoding (use UTF-8) |

---

## Sub-phase details

### 1a

#### Build
Function that accepts an image path and copies it to `jobs/<id>/input`

#### Pass check
File saved, job ID generated

#### Known issues
Duplicate names, special characters

### 1b

#### Build
Convert HEIC/WebP/JPEG to PNG

#### Pass check
All formats open and save correctly

#### Known issues
HEIC needs `pillow-heif`

### 1c

#### Build
Fix EXIF rotation

#### Pass check
Phone photos appear upright

#### Known issues
Sideways photos

### 1d

#### Build
Quality checks: min 800px, blur score, max file size

#### Pass check
Tiny and blurry photos rejected with a clear message

#### Known issues
Blur threshold needs tuning on your set

### 1e

#### Build
Product details schema (name, price, features, target customer, language, tone)

#### Pass check
Missing fields give a readable error

#### Known issues
Users entering vague or very long text

### 1f

#### Build
Output a clean `product.json`

#### Pass check
All 10 products produce valid JSON, bad ones fail cleanly

#### Known issues
Non-English text encoding (use UTF-8)
