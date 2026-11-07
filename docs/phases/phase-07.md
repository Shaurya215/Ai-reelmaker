# Phase 7: Text and captions

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 7a | Fonts for Latin, Devanagari, Gujarati | All three scripts render correctly | Missing glyphs show as boxes |
| 7b | Static overlays: product name, price badge | Readable on a phone screen | Long product names overflow |
| 7c | Safe-area rules for Instagram/Shorts UI | Nothing hidden under buttons or captions | Different apps have different UI overlays |
| 7d | faster-whisper word timestamps | Timestamps match the voice | Wrong words in Hindi/Gujarati (consider using the script text instead and aligning to it) |
| 7e | Word-by-word animated captions (ASS subtitles) | Highlight follows the voice | Timing drift, ASS style escaping |
| 7f | Closing CTA card ("Order now" plus contact) | Last 2s shows clear CTA | Contact details missing from input |

---

## Sub-phase details

### 7a

#### Build
Fonts for Latin, Devanagari, Gujarati

#### Pass check
All three scripts render correctly

#### Known issues
Missing glyphs show as boxes

### 7b

#### Build
Static overlays: product name, price badge

#### Pass check
Readable on a phone screen

#### Known issues
Long product names overflow

### 7c

#### Build
Safe-area rules for Instagram/Shorts UI

#### Pass check
Nothing hidden under buttons or captions

#### Known issues
Different apps have different UI overlays

### 7d

#### Build
faster-whisper word timestamps

#### Pass check
Timestamps match the voice

#### Known issues
Wrong words in Hindi/Gujarati (consider using the script text instead and aligning to it)

### 7e

#### Build
Word-by-word animated captions (ASS subtitles)

#### Pass check
Highlight follows the voice

#### Known issues
Timing drift, ASS style escaping

### 7f

#### Build
Closing CTA card ("Order now" plus contact)

#### Pass check
Last 2s shows clear CTA

#### Known issues
Contact details missing from input
