# Phase 11: Backend and queue

| Step | Build | Test and pass | Watch for |
|---|---|---|---|
| 11a | FastAPI app with `POST /generate` accepting upload | File and details received | Upload size limits |
| 11b | SQLite job table (queued, running, done, failed) | Job states update correctly | |
| 11c | Single background worker running the pipeline | One job completes end to end via API | Worker crash leaves job stuck, add timeout |
| 11d | `GET /status/{id}` and `GET /download/{id}` | Progress and download work | |
| 11e | Concurrency test: 5 simultaneous requests | No lost jobs, one render at a time | Memory crash from parallel renders |
| 11f | Cleanup of old files and failed jobs | Disk does not fill up | |

---

## Sub-phase details

### 11a

#### Build
FastAPI app with `POST /generate` accepting upload

#### Pass check
File and details received

#### Known issues
Upload size limits

### 11b

#### Build
SQLite job table (queued, running, done, failed)

#### Pass check
Job states update correctly

#### Known issues
(none)

### 11c

#### Build
Single background worker running the pipeline

#### Pass check
One job completes end to end via API

#### Known issues
Worker crash leaves job stuck, add timeout

### 11d

#### Build
`GET /status/{id}` and `GET /download/{id}`

#### Pass check
Progress and download work

#### Known issues
(none)

### 11e

#### Build
Concurrency test: 5 simultaneous requests

#### Pass check
No lost jobs, one render at a time

#### Known issues
Memory crash from parallel renders

### 11f

#### Build
Cleanup of old files and failed jobs

#### Pass check
Disk does not fill up

#### Known issues
(none)
