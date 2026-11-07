# ISSUES

Format: `date | sub-phase | product | what happened | fix`

| date | sub-phase | product | what happened | fix |
|---|---|---|---|---|
| 2026-11-07 | 0a | n/a | `git init` was run in the parent folder (`Claude Projects/`) instead of `Reelmaker/`; `git status` showed every file as `Reelmaker/...`, and a duplicate `PLAN_SOURCE.md` had been left at the project root | removed the parent `.git`, `cd`'d into `Reelmaker/`, ran `git init -b main` there, removed the duplicate root `PLAN_SOURCE.md`. Nothing had been pushed. Lesson: run `pwd` and `ls -a` before `git init` |
| 2026-11-07 | 0a | n/a | Ubuntu 24.04 ships Python 3.12.3 by default; `python3.11` is not in the default apt repos, so installing it directly failed | added the deadsnakes PPA and installed `python3.11` + `python3.11-venv`; verified 3.11.18 inside `venv/`. Lesson: check `python3.11 --version` before the sub-phase starts |
