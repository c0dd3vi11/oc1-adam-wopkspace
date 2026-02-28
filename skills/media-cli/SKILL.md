---
name: media-cli
description: Download, trim, crop, transcode, and repack local video/audio files via yt-dlp + ffmpeg. Use when asked to process media files, especially YouTube links, black-bar removal, aspect fixes, codec/container conversion, and Telegram-friendly export.
---

# Media CLI

## Tool paths

Use these binaries by absolute path:

- `/home/adam/.openclaw/workspace/bin/yt-dlp`
- `/home/adam/.openclaw/workspace/bin/ffmpeg`
- `/home/adam/.openclaw/workspace/bin/ffprobe`

## Default workflow

1. Download source with `yt-dlp`.
2. Inspect media with `ffprobe`.
3. Process with `ffmpeg` (crop/trim/transcode as requested).
4. Verify output stream parameters with `ffprobe`.
5. Send result file to user and keep intermediate files temporary.

## Update policy

- It is allowed to update/replace `yt-dlp`, `ffmpeg`, and `ffprobe` binaries when needed.
- After update, run `--version` check before use.
