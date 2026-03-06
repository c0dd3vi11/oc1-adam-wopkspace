---
name: voice-command-transcriber
description: Transcribe inbound audio/voice messages (ogg/opus/m4a/mp3/wav) into text and treat the transcript as the user’s command. Use when a user sends audio instead of text, especially in Telegram chats. Auto-transcribe first, then execute the request from transcript; ask for clarification only when confidence is low, text is unclear, or the requested action is sensitive/destructive.
---

# Voice Command Transcriber

Transcribe user audio locally with `faster-whisper`, then continue the turn as if the user typed that text.

## Workflow

1. Detect inbound audio attachment.
2. Transcribe it with the bundled script.
3. If transcript is clear, execute the request immediately.
4. If transcript is uncertain/garbled, send a short clarification question with the best-effort transcript.
5. For sensitive actions (deletion, external posting, irreversible changes), require explicit confirmation even if transcript is clear.

## Command

Use this command from workspace root:

```bash
uv run --with faster-whisper \
  skills/voice-command-transcriber/scripts/transcribe_audio.py \
  <audio_path> --json
```

Parse JSON fields:
- `text` — full transcript
- `language`
- `language_probability`
- `segments[]`

## Decision Rules

- Treat transcript as reliable when:
  - `text` is non-empty, and
  - `language_probability >= 0.70`, and
  - transcript is semantically coherent.
- If below threshold or incoherent:
  - ask user to confirm/repeat,
  - include your best guess in quotes.
- If multiple plausible interpretations exist:
  - offer 2–3 short options and ask which one to run.

## Response Style

- Keep it short.
- First line: recognized transcript (only when useful or user asked).
- Then perform requested action/result.
- Do not dump timestamps/segments unless user asks.
