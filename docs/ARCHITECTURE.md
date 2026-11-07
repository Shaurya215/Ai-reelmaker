# ARCHITECTURE (planned)

This describes the planned system shape from `docs/PLAN_SOURCE.md`. It is a design reference, not a record of what is built yet — see `docs/STATE.md` for actual progress.

## Product-image preservation
The uploaded product photo is the one source of truth for the product's real appearance. It is never regenerated, redrawn, or passed through a generative image model. The pipeline instead:
- keeps the original upload untouched on disk,
- produces a background-removed cutout (separate layer) via rembg,
- composites that cutout over AI/stock/gradient backgrounds and motion as a distinct layer,
- optionally checks AI-generated motion (Phase 10) against the original product via similarity scoring (SSIM/CLIP) before accepting it, falling back to non-AI motion otherwise.

## Video pipeline (per PLAN_SOURCE phases)
1. Input & validation (Phase 1): accept photo + product details, normalize format/orientation, quality-gate, emit `product.json`.
2. Ad brief (Phase 2): LLM adapter turns product details into a structured brief (hook, benefits, tone, CTA, scenes), with a claim checker against user-supplied facts only.
3. Voiceover (Phase 3): TTS adapter renders the brief's script to audio, fit to target length, loudness-normalized.
4. Product image prep (Phase 4): background removal, mask cleanup, crop/pad, upscale, placed on a 1080x1920 transparent canvas.
5. Background & scene (Phase 5): backgrounds generated/sourced, product placed with grounding, shadow, and color match; multiple variants scored and selected.
6. Motion (Phase 6): FFmpeg-driven zoom/pan/parallax/transitions, scene timing driven by voiceover.
7. Text & captions (Phase 7): multi-script font rendering, static overlays, safe-area rules, word-level animated captions from faster-whisper timestamps, closing CTA.
8. Final render & music (Phase 8): mux video/audio, duck music under voice, loudness-normalize, export H.264/AAC 1080x1920.
9. Quality checker (Phase 9): automated technical/audio/visual checks with one retry before a pass/fail report.
10. Optional AI motion (Phase 10, non-core): image-to-video adapter behind the same integrity check described above.
11. Backend & queue (Phase 11): FastAPI + SQLite job table + single background worker exposing generate/status/download.
12. Web UI (Phase 12): upload form, progress polling, preview/download, mobile-first.

## Provider adapters
Every external/vendor capability (LLM, TTS, background removal, image-to-video, stock photos) sits behind a narrow adapter interface in `providers/` (e.g. `synthesize(text, voice) -> path`, `generate(prompt) -> text`). Application code calls only the adapter, never the vendor SDK directly. Swapping a free provider for a paid one (Phase 14) is a `config.yaml` change, not a code change.

## SQLite
Planned as the job store (Phase 11b): a single table tracking job id, state (queued/running/done/failed), and references to the job's working directory under `jobs/`. No other persistence is planned at this stage.

## FFmpeg
Used throughout for: image-to-video base clips, zoom/pan/parallax motion, scene transitions, caption burn-in (ASS subtitles), audio muxing/ducking/loudness normalization, and final export. All FFmpeg invocations are expected to go through a thin wrapper rather than being called ad hoc from multiple places.

## Configuration-driven provider selection
`config.yaml` (created in Phase 0c) selects which adapter implementation backs each stage (e.g. LLM: Gemini vs Groq vs a future paid model; TTS: Piper vs a future paid voice). Adapters read their own settings from this file; application code is provider-agnostic.

## Future decisions (not yet made — see docs/DECISIONS.md once resolved)
- Temporary-file cleanup policy for `jobs/`.
- Failed-job recovery/retry behavior.
- SQLite backup strategy.
- Output retention period for rendered videos.
- Upload-size limits.
- Concurrent-job handling (single worker vs pool) under the 8GB RAM target.

## Resource constraint
Target development machine has 8GB RAM. The pipeline is planned to load AI models (rembg, TTS, whisper, any image-to-video model) sequentially per stage rather than holding all of them in memory at once.
