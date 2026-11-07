# Phase 9: Automatic quality checker

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 9a | Technical checks: resolution, duration, codec | Bad files are caught | |
| 9b | Black and frozen frame detection | Seeded bad clip is caught | False alarms on dark products |
| 9c | Audio checks: loudness range, silence, clipping | Seeded bad audio is caught | |
| 9d | Product visibility: product occupies at least X% of frame in each scene | Cropped product is caught | Choosing X |
| 9e | Text safe-area and overflow check | Overflowing text is caught | |
| 9f | Auto-retry once with different settings, then produce a pass/fail report | Report is readable by a non-technical person | Infinite retry loops |

---

## Sub-phase details

### 9a

#### Build
Technical checks: resolution, duration, codec

#### Pass check
Bad files are caught

#### Known issues
(none)

### 9b

#### Build
Black and frozen frame detection

#### Pass check
Seeded bad clip is caught

#### Known issues
False alarms on dark products

### 9c

#### Build
Audio checks: loudness range, silence, clipping

#### Pass check
Seeded bad audio is caught

#### Known issues
(none)

### 9d

#### Build
Product visibility: product occupies at least X% of frame in each scene

#### Pass check
Cropped product is caught

#### Known issues
Choosing X

### 9e

#### Build
Text safe-area and overflow check

#### Pass check
Overflowing text is caught

#### Known issues
(none)

### 9f

#### Build
Auto-retry once with different settings, then produce a pass/fail report

#### Pass check
Report is readable by a non-technical person

#### Known issues
Infinite retry loops
