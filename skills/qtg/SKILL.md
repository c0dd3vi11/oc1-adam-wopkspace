---
name: qtg
description: Use Telegram via real user account Adam through q-tools/Telethon daemon. Use when Bot API is limited, bot lacks rights, entity/edit behavior differs between bot and user API, or user-context Telegram actions are required.
---

# qtg

## Read first

- `/home/adam/.openclaw/workspace/docs/telegram-real-user-adam.md`
- `/home/adam/dev/tools/q-tools/AGENTS.md`

## Command surface

Primary CLI:

- `/home/adam/dev/tools/q-tools/bin/q tg ...`

Typical actions include status/ping, raw/tl calls, send/edit/read flows supported by q-tools + telethon-daemon.

## Workflow

1. Try regular bot path first when sufficient.
2. If blocked by Bot API/permissions, switch to `q tg` (real user Adam).
3. Verify result by reading message/chat state after action.
4. Report outcome with links/ids when relevant.

## Safety

- Do not perform public/external actions without explicit user ask.
- Ask before bulk/destructive actions.
- Watch for race conditions with parallel cron/manual tasks.
