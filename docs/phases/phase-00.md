# Phase 0: Setup

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 0a | Python 3.11, venv, Git repo | `python --version` works, first commit pushed | Wrong Python on PATH |
| 0b | Install FFmpeg | `ffmpeg -version` prints in terminal | PATH on Windows |
| 0c | Folder structure, `config.yaml`, `.env`, `issues.md` | Config loads from Python without errors | API keys committed to Git (add `.env` to `.gitignore`) |
| 0d | FFmpeg command: 1 image → 5s MP4 | Plays on your phone | Odd image sizes (need even width and height) |

---

## Sub-phase details

### 0a

#### Build
Python 3.11, venv, Git repo

#### Pass check
`python --version` works, first commit pushed

#### Known issues
Wrong Python on PATH

### 0b

#### Build
Install FFmpeg

#### Pass check
`ffmpeg -version` prints in terminal

#### Known issues
PATH on Windows

### 0c

#### Build
Folder structure, `config.yaml`, `.env`, `issues.md`

#### Pass check
Config loads from Python without errors

#### Known issues
API keys committed to Git (add `.env` to `.gitignore`)

### 0d

#### Build
FFmpeg command: 1 image → 5s MP4

#### Pass check
Plays on your phone

#### Known issues
Odd image sizes (need even width and height)
