# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

### Media CLI (local)

- `yt-dlp`: `/home/adam/.openclaw/workspace/bin/yt-dlp`
- `ffmpeg`: `/home/adam/.openclaw/workspace/bin/ffmpeg`
- `ffprobe`: `/home/adam/.openclaw/workspace/bin/ffprobe`

Quick version check:

```bash
/home/adam/.openclaw/workspace/bin/yt-dlp --version
/home/adam/.openclaw/workspace/bin/ffmpeg -version | head -n1
```

Quick update recipe:

```bash
cd /home/adam/.openclaw/workspace
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o bin/yt-dlp && chmod +x bin/yt-dlp
curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz -o .cache/tooling/ffmpeg.tar.xz
mkdir -p .cache/tooling/ffmpeg-extract && tar -xf .cache/tooling/ffmpeg.tar.xz -C .cache/tooling/ffmpeg-extract
FFDIR=$(find .cache/tooling/ffmpeg-extract -maxdepth 1 -type d -name 'ffmpeg-*-amd64-static' | head -n1)
cp "$FFDIR/ffmpeg" "$FFDIR/ffprobe" bin/ && chmod +x bin/ffmpeg bin/ffprobe
```

### Privileges / sudo

- User `adam` has passwordless sudo configured on this host.
- Prefer running privileged commands via `sudo -n ...` from normal `exec` when needed.
- Important: OpenClaw tool flag `elevated=true` can still be blocked by gateway policy even when host sudo itself works.
