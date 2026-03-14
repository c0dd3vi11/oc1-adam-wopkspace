---
name: youtube-channel-analysis
description: Analyze a YouTube channel by publishing timeline (date-linked), topic distribution, monthly posting frequency, and top videos; generate a full markdown report and optionally send the report file to Anton in Telegram. Use when user asks to analyze a YouTube channel, audit all channel videos, make a date-based breakdown, or requests phrases like "проанализируй канал", "анализ всех роликов", "с привязкой по дате", "сделай отчёт по YouTube каналу".
---

# YouTube Channel Analysis

Use this skill to create a full channel report from YouTube URL (`@handle`, `/channel/...`, `/videos`, or playlist view).

## Workflow

1. Collect channel video metadata with:
   - `/home/adam/.openclaw/workspace/bin/yt-dlp --dump-single-json <URL>`
2. Build report via script:
   - `python3 scripts/build_report.py --input <json> --out <report.md>`
3. Verify report header and top section by reading first ~80 lines.
4. If user asked to send file, send `report.md` via `message` tool as attachment.

## Required output

Report must include:

- Total videos and analyzed date range
- Posting frequency by month
- Theme distribution by title heuristics
- Top videos by views
- Full chronology: date, theme, title, views, URL

## Commands

```bash
# 1) Fetch channel metadata
/home/adam/.openclaw/workspace/bin/yt-dlp --dump-single-json "https://youtube.com/@channel/videos" > /home/adam/.openclaw/workspace/.tmp_channel.json

# 2) Build markdown report
python3 /home/adam/.openclaw/workspace/skills/youtube-channel-analysis/scripts/build_report.py \
  --input /home/adam/.openclaw/workspace/.tmp_channel.json \
  --out /home/adam/.openclaw/workspace/reports/youtube_channel_analysis_<YYYY-MM-DD>.md
```

## Notes

- Prefer `--dump-single-json` to preserve `upload_date` in one payload.
- If `view_count` is missing, treat it as `0`.
- Keep chronology sorted oldest → newest.
- Keep report language aligned with user language (Russian by default for Anton).
