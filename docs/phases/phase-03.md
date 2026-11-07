# Phase 3: Voiceover

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 3a | Piper TTS for English | Clean audio file from text | Voice model download size |
| 3b | TTS adapter interface (`synthesize(text, voice) -> path`) | Swapping provider is a config change only | Hardcoding Piper details everywhere |
| 3c | Hindi and Gujarati voices | Log which voices are acceptable | Free Gujarati voices may be poor, so decide your fallback |
| 3d | Pronunciation dictionary for brand names | Brand names sound right | Needs manual overrides |
| 3e | Fit the script to the target length (20-30s) | Audio lands within the range | Too long: trim the script, not speed up the audio |
| 3f | Normalize loudness | Same volume across all 10 clips | Clipping |

---

## Sub-phase details

### 3a

#### Build
Piper TTS for English

#### Pass check
Clean audio file from text

#### Known issues
Voice model download size

### 3b

#### Build
TTS adapter interface (`synthesize(text, voice) -> path`)

#### Pass check
Swapping provider is a config change only

#### Known issues
Hardcoding Piper details everywhere

### 3c

#### Build
Hindi and Gujarati voices

#### Pass check
Log which voices are acceptable

#### Known issues
Free Gujarati voices may be poor, so decide your fallback

### 3d

#### Build
Pronunciation dictionary for brand names

#### Pass check
Brand names sound right

#### Known issues
Needs manual overrides

### 3e

#### Build
Fit the script to the target length (20-30s)

#### Pass check
Audio lands within the range

#### Known issues
Too long: trim the script, not speed up the audio

### 3f

#### Build
Normalize loudness

#### Pass check
Same volume across all 10 clips

#### Known issues
Clipping
