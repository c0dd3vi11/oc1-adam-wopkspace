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

### SSH hosts

- `msk1` → `80.249.151.50`, user `root`, key `~/.ssh/msk1_ed25519`
- SSH alias configured in `~/.ssh/config`; quick check: `ssh msk1 'hostname && id -un'`
- На `msk1` установлен `3x-ui` (учитывать при задачах по VPN/proxy панели).

### WireGuard geo egress map (operational)

- `wgge1` → DE (Frankfurt) → `80.66.87.163`
- `wgmsk1` → RU (Moscow) → `80.249.151.50`
- `wgusa1` → US (Dallas) → `150.241.122.203`

Notes:
- Антон также использует эти IP; на `DE` и `US` уже завязаны рабочие сценарии.
- Быстрый гео-запрос: `wg-ipinfo <iface>`
- Произвольный запрос через нужный регион: `wg-curl <iface> <url> [curl args...]`

### ⚠️ Telegram newline rule (CRITICAL)

- For `q tg` / Telethon JSON payloads, **never** send literal `\\n` inside text.
- Always send **real newline characters** (actual line breaks) in message text.
- Pre-send check: if text contains `\\n`, convert to real newlines before sending.
- This is mandatory for all channel posts/captions and approval drafts.

### Phone proxy via Anton's Termux (reverse SOCKS)

- Skill: `/home/adam/.openclaw/workspace/skills/phone-proxy/SKILL.md`
- Working phone command:
  ```bash
  ssh -NT -p 18754 -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -R 1081 adam@185.28.175.67
  ```
- Host-side check:
  ```bash
  curl -sS --socks5-hostname 127.0.0.1:1081 https://api.ipify.org
  ```
- Do not use `-R 1081:localhost:1080` unless local SOCKS server is running on phone:1080.

### VLESS+REALITY (msk1) local quick access

- local service: `sing-box-msk.service` (autostart enabled)
- SOCKS profiles:
  - `127.0.0.1:12001` → profile `cf` (`vless-reality-oc1adam-msk`, SNI `www.cloudflare.com`)
  - `127.0.0.1:12002` → profile `vk` (`vless-reality-vk-msk`, SNI `vk.com`)
- quick commands:
  - `vless-ipinfo cf`
  - `vless-ipinfo vk`
  - `vless-curl cf <url>`
  - `vless-curl vk <url>`
