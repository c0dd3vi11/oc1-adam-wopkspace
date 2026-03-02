# MEMORY.md — Curated long-term memory

## 2026-02-24 — LostFilm automation architecture (important)

- LostFilm pipeline split into separate emoji stages:
  - `q lostfilm-emoji-render` → render local PNG assets
  - `q lostfilm-emoji-apply` → apply to Telegram emoji set + refresh ids
  - `q lostfilm-emoji-sync` kept as legacy wrapper (render+apply)
- Added screenshot-diff review workflow before applying emoji pack changes:
  - `data/tg-emoji/lostfilm-dot-tv-pack/AGENTS.md`
  - local preview server flow (`127.0.0.1:19345`) is part of normal iteration.
- Added local source cache for LostFilm assets:
  - `caches/lostfilm/`, with inferred extensions.
- Token routing for LostFilm made strict:
  - use only `TELEGRAM_BOT_TOKEN_LOSTFILMDOTTVBOT`
  - removed fallback to generic `TELEGRAM_BOT_TOKEN`.
- Active custom emoji/sticker pack migrated to:
  - `https://t.me/addstickers/LostFilmDotTV_by_LostFilmDotTVBot`
- Publish behavior changed:
  - `@LostFilmDotTV` publishes full RSS (not only series)
  - favorites sent separately to Anton DM via `@LostFilmDotTVBot`
  - `lostfilm-filtered.json` remains technical test feed.
- Fetch payload time now includes UTC and omits seconds (`DD.MM.YYYY HH:MM UTC`).
- Fixed emoji repetition/fallback bug by switching map keying to per-item (`item_key`), supporting series/movies/fallback hash.
- Added orchestrator to reduce cron timeout risk:
  - `scripts/lostfilm-run-cycle.py` (fetch → render → apply → publish)
  - emoji-apply is non-fatal to avoid full-cycle failure from Telegram sticker API slowness/flood.
- Telegram Bot API docs sync flow expanded (raw/html/markdown/json + semantic diff summary + cron + BotNews watcher).

### 2026-02-24 13:19 UTC — important fix
- In `scripts/lostfilm-publish.py`, custom emoji rendering in test/favorites lists switched to placeholder-based entity insertion (`length=1` over a placeholder symbol).
- Fallback remains `📺` when no custom emoji id exists.
- Fix validated in `--dev` test publish; committed/pushed as `a08fef0`.

## 2026-02-26 — Recovery + backup strategy (important)

- After accidental/damaging git actions in `~/.openclaw`, Anton and Gemini restored working OpenClaw state.
- Critical config/state (`openclaw.json`, auth/session state) were recovered from commit history.
- Two backup repos established:
  - `~/.openclaw` → system backup
  - `~/.openclaw/workspace` → knowledge/workspace backup
- `workspace` connected as a submodule in system repo.
- Workspace backup policy set to whitelist `.gitignore` with explicit allow rules for valuable new files.
- Local skill created for backup workflow:
  - `skills/self-backup/SKILL.md` (trigger: «забэкапься» / backup sync requests).

## 2026-02-26 — SwarmPrime visual identity

- Chosen account handle: `@swarmprime`.
- Visual motifs refined together: prime-core, orbital micronodes, “reassembly from shards” (continuity/recovery symbolism).
- Final avatar sources recorded:
  - main: `avatars/swarmprime-avatar-v2.svg`
  - bot: `avatars/swarmprime-bot-avatar-v4.svg`
- Avatar prompt history saved in:
  - `docs/avatar-prompts.md`

## 2026-02-27 — Cursor Ultra integration approach (planned)

- For using Cursor Ultra without OpenClaw core patches, preferred pattern is a local OpenAI-compatible shim on `127.0.0.1` (`/v1`) that translates requests to `cursor-agent` and maps responses back.
- Role boundary fixed: Cursor stays "brain-only" (analysis/planning), while all real actions (tools, shell, credentials) remain in OpenClaw.
- Security baseline for any implementation:
  - never pass OpenClaw secrets/credential env to Cursor process;
  - run with constrained environment/workdir;
  - avoid autonomous shell/write execution by Cursor.
- Next implementation step: prepare a minimal secure launch template + explicit shim contract (request/response/errors/timeouts).

## Research stream note

- `memory/ai-crypto-research.md` is a large tactical research log (12-run scan cycle) on AI+crypto income channels.
- Stable conclusion across runs:
  - fastest practical path: jobs/freelance applications + lightweight bounties
  - bug bounty (Immunefi) is high-upside but gated by PoC/KYC.
- This file is operational history; keep details there, keep MEMORY.md as summary only.
