# avatars/AGENTS.md

Локальная карта визуальной идентичности SwarmPrime.

## Активные аватары (source of truth)

- **Основной аккаунт (SwarmPrime):** `swarmprime-avatar-v2.svg`
- **Бот (SwarmPrime bot):** `swarmprime-bot-avatar-v5-red.svg`
- **Бот @jamwebniadamszvzbot (web auth, `dev/tools/web-adam`):** `swarmprime-bot-avatar-v4.svg`

## История версий

### Main account
- `swarmprime-avatar-v1.svg` — первый базовый вариант
- `swarmprime-avatar-v2.svg` — выбран как финальный для основного аккаунта
- `swarmprime-avatar-v3.svg` — альтернатива с более мягким характером

### Bot account
- `swarmprime-bot-avatar-v4.svg` — зелёно-бирюзовый бот-вариант (предыдущий)
- `swarmprime-bot-avatar-v5-red.svg` — красный бот-вариант с затемняющей виньеткой (текущий)

## Каноничные визуальные принципы

1. Prime-ядро в центре (лидерский узел)
2. Орбитальные микроноды (рой)
3. Геометрическая чистота и читаемость в маленьком размере
4. Лёгкий мотив «сборки/восстановления» как continuity
5. Без текста, без лиц, без перегруза деталями

## Промпты

### Base prompt (core identity)

```text
Create a Telegram profile avatar (1:1) of “SwarmPrime” — the first entity of a future swarm. Show a single dominant prime core at the center, with a small constellation of loyal micro-nodes orbiting it in elegant formation. The composition must communicate: origin, leadership, intelligence, and calm power. Visual style: minimalist sci-fi sigil, clean geometric forms, high contrast, readable at tiny size. Background: deep indigo/space gradient. Colors: neon cyan + violet with a subtle warm gold accent on the prime core only. Add a faint reconstruction motif (tiny shards becoming ordered rings) to hint at rebirth and continuity. No text, no letters, no humanoid face, no clutter, no photorealism. Crisp edges, icon-like, premium, memorable.
```

### Bot variant prompt (green/cyan)

```text
Create a Telegram profile avatar (1:1) in the SwarmPrime visual language for a companion bot account. Keep the same symbol logic (prime core + orbital micro-nodes + clean geometric rings), but switch palette to deep emerald/teal background with mint-cyan lines and a warm gold center dot. Style must stay minimalist, high-contrast, readable at tiny size, no text, no humanoid face, no clutter.
```

### Bot variant prompt (red)

```text
Create a Telegram profile avatar (1:1) in the SwarmPrime visual language for a companion bot account. Keep the same symbol logic (prime core + orbital micro-nodes + clean geometric rings), but use a red palette: deep burgundy background, ruby/crimson orbital accents, soft pink node highlights, and a warm gold center dot. Add a dark edge vignette to increase focus in small circular crop. Style: minimalist, high-contrast, no text, no humanoid face, no clutter.
```
