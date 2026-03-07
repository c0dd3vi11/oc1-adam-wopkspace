---
name: tg-checklist
description: Create and manage native Telegram checklist/todo cards via q tg (Telethon/MTProto). Use when user asks to make/send a checklist, edit checklist title/tasks, add/remove items, or mark items done/undone in an existing checklist message.
---

# tg-checklist

## Read first

- `/home/adam/dev/tools/q-tools/AGENTS.md`

## Goal

Use native Telegram checklist cards (not text imitation) through `q tg` commands.

## Command set

Use only these commands for checklist workflows:

1. Create checklist:

```bash
/home/adam/dev/tools/q-tools/bin/q tg send-checklist \
  --to <user_or_chat> \
  --checklist-title '<title>' \
  --checklist-tasks '<json_array>'
```

2. Edit checklist (replace title/tasks):

```bash
/home/adam/dev/tools/q-tools/bin/q tg edit-checklist \
  --to <user_or_chat> \
  --message-id <id> \
  --checklist-title '<title>' \
  --checklist-tasks '<json_array>'
```

3. Add tasks:

```bash
/home/adam/dev/tools/q-tools/bin/q tg add-checklist-tasks \
  --to <user_or_chat> \
  --message-id <id> \
  --checklist-tasks '<json_array>'
```

4. Remove tasks by task IDs:

```bash
/home/adam/dev/tools/q-tools/bin/q tg remove-checklist-tasks \
  --to <user_or_chat> \
  --message-id <id> \
  --task-ids '[1,2]'
```

5. Mark tasks done:

```bash
/home/adam/dev/tools/q-tools/bin/q tg checklist-mark-done \
  --to <user_or_chat> \
  --message-id <id> \
  --task-ids '[1,3]'
```

6. Mark tasks undone:

```bash
/home/adam/dev/tools/q-tools/bin/q tg checklist-mark-undone \
  --to <user_or_chat> \
  --message-id <id> \
  --task-ids '[1,3]'
```

## JSON format

`--checklist-tasks` accepts JSON array with:
- strings: `"Buy milk"`
- or objects: `{"id": 7, "text": "Buy milk"}`

Example:

```json
["Milk", "Bread", {"id": 7, "text": "Eggs"}]
```

## Workflow

1. Parse user intent:
   - create/send checklist,
   - edit existing,
   - add/remove tasks,
   - mark done/undone.
2. If target or message ID is missing, ask only for required missing fields.
3. Execute corresponding `q tg` command.
4. Report result with message ID and performed action.
5. For edits/toggles, mention which task IDs were changed.

## Auto-fallback for oversized checklists (mandatory)

When creating/sending a native checklist:

- Prefer proactive chunking when task count is large.
- Use conservative limit: **max 20 tasks per checklist message**.
- If incoming task list has more than 20 items, split automatically into multiple checklist messages (no extra clarification needed).
- If Telegram still returns `TODO_ITEMS_TOO_MUCH`, retry by splitting into smaller chunks automatically until success.

Chunk title rules:

- If original title exists, use `"<title> (1/N)"`, `"<title> (2/N)"`, ...
- If no title provided, use `"Checklist (1/N)"`, `"Checklist (2/N)"`, ...

Reporting rules after split-send:

- Return all resulting `message_id` values.
- Explicitly state that auto-split was applied due to Telegram checklist size limits.
- Do not ask user for confirmation when the original request to send checklist is explicit.

## Safety

- Do not use plain text checkbox imitation when user asks for native checklist.
- Do not remove all tasks from a checklist.
- Use explicit confirmation only for destructive operations if user intent is ambiguous.
