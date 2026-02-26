---
name: self-backup
description: Быстрое резервное копирование и синхронизация состояния ассистента в двух репозиториях (`~/.openclaw` и `~/.openclaw/workspace`). Использовать, когда владелец (Антон, доверенные Telegram ID) просит: «забэкапься», «сделай бэкап себя», «обнови backup-репы», «синхронизируй бэкап».
---

# Self Backup

1. Проверить изменения в обоих репозиториях:
   - `~/.openclaw`
   - `~/.openclaw/workspace`

2. В `~/.openclaw/workspace`:
   - Коммитить только whitelist-данные (см. `.gitignore` и `WORKSPACE_DATA_CLASSIFICATION.md`).
   - Если важный новый файл не проходит whitelist — добавить явное исключение `!path` в `.gitignore`, затем коммитить файл и изменение `.gitignore` вместе.

3. В `~/.openclaw`:
   - Убедиться, что секретные пути из `.gitattributes` остаются под `git-crypt`.
   - Не выполнять destructive-операции (`reset --hard`, rewrite history, force-push), кроме явного запроса владельца.

4. Перед push:
   - Проверить `git status` в каждом репозитории.
   - Проверить, что нет случайных plaintext-секретов в нешифруемых файлах.

5. Выполнить commit/push в порядке:
   - `workspace` (сначала)
   - затем `~/.openclaw` (чтобы обновить pointer сабмодуля)

6. Отчитаться кратко:
   - какие коммиты созданы,
   - куда запушено,
   - что осталось untracked/отложено и почему.

## Где читать подробнее

- `/home/adam/.openclaw/README.md` (восстановление, git-crypt, политика)
- `/home/adam/.openclaw/workspace/WORKSPACE_DATA_CLASSIFICATION.md` (ценные/неценные данные)
- `/home/adam/.openclaw/workspace/AGENTS.md` (правила backup-политики workspace)
