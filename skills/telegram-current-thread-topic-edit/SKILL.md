---
name: telegram-current-thread-topic-edit
description: >-
  Edit Telegram topic title and emoji for the current thread using inbound
  message_thread_id/topic_id from incoming metadata. Keep titles
  mobile-friendly (target <=18 chars, hard cap 24). Use when user asks to
  rename/update/clarify the current topic/thread title or icon, including
  phrases like «переименуй этот топик/тред», «поставь эмоджи этому топику»,
  «сделай topic-edit для текущего треда», «обнови название топика»,
  «актуализируй название топика», «уточни название треда»,
  «уточни заголовок беседы», «обнови в беседе заголовок». Use this skill for
  any equivalent wording about changing the current thread topic title/icon.
---

# Telegram Current Thread Topic Edit

Use this skill to reliably edit the **current** Telegram topic (thread), not a different one.

## Required Inputs

From inbound metadata, use:
- `chat_id`
- `message_thread_id` (or `topic_id`)

If `message_thread_id` is missing, ask user to send one message in the target topic and retry.

## Title Length Rule (mobile-first)

From UI constraints (like Telegram's left topic list on phone), keep titles compact:
- target: `<= 18` characters
- hard cap: `24` characters
- prefer 1–2 short words; avoid long phrases

## Required Parameters (smart defaults)

Default behavior (unless user explicitly says otherwise):
- Choose `name` (new topic title) yourself based on the current conversation context.
- Choose `icon_custom_emoji_id` (topic icon) yourself from available topic icons.

If user explicitly provides title and/or emoji, use their values.
If user asks to choose manually, pick concise, context-relevant options and apply without extra clarification.

## Execute topic-edit

Token resolution order in script:
1) `TELEGRAM_BOT_TOKEN*` env vars
2) `/home/adam/.config/q-tools/secrets.env`

Run:

```bash
python3 skills/telegram-current-thread-topic-edit/scripts/edit_forum_topic.py \
  --chat-id <chat_id> \
  --thread-id <message_thread_id> \
  --name "<new title>" \
  --icon-custom-emoji-id "<custom_emoji_id>"
```

## Discover available topic icons

```bash
python3 skills/telegram-current-thread-topic-edit/scripts/edit_forum_topic.py \
  --chat-id <chat_id> \
  --thread-id <message_thread_id> \
  --name "tmp" \
  --list-icons
```

Then pick `custom_emoji_id` matching requested emoji.

## Safety/Behavior

- Always prefer current inbound `message_thread_id`; do not reuse old thread IDs.
- Confirm back to user: edited thread ID, title, and emoji.
- For ambiguous requests, propose 2–3 short title options before applying.
