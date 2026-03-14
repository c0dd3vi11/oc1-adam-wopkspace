#!/usr/bin/env python3
import argparse
import collections
import datetime as dt
import json
from pathlib import Path


def classify(title: str) -> str:
    t = (title or "").lower()
    if any(k in t for k in ["как устроен код", "python", "jupyter", "vps", "установка", "часть"]):
        return "Обучение/разбор кода"
    if any(k in t for k in ["ai", "ии", "agent", "агент", "автомат", "автопилот", "deepseek"]):
        return "AI/автоматизация"
    if any(k in t for k in ["индикатор", "atr", "cvd", "дельт", "risk", "риск", "анализ"]):
        return "Индикаторы/риск-менеджмент"
    if any(k in t for k in ["solana", "meteora", "orca", "xemm", "grid", "pmm", "bollinger", "supertrend", "hummingbot"]):
        return "Стратегии Hummingbot/DeFi"
    return "Рынок/концепции"


def parse_upload_date(raw: str):
    if not raw or len(raw) != 8:
        return None
    return dt.date(int(raw[:4]), int(raw[4:6]), int(raw[6:8]))


def main():
    p = argparse.ArgumentParser(description="Build YouTube channel markdown analysis report")
    p.add_argument("--input", required=True, help="Path to yt-dlp --dump-single-json output")
    p.add_argument("--out", required=True, help="Output markdown report path")
    args = p.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries", [])
    items = []
    for e in entries:
        d = parse_upload_date(e.get("upload_date"))
        if not d:
            continue
        vid = e.get("id")
        items.append({
            "date": d,
            "title": e.get("title", ""),
            "views": e.get("view_count") or 0,
            "id": vid,
            "url": f"https://youtu.be/{vid}" if vid else "",
        })

    items.sort(key=lambda x: x["date"])
    if not items:
        raise SystemExit("No videos with upload_date found")

    by_month = collections.Counter((x["date"].year, x["date"].month) for x in items)
    by_theme = collections.Counter(classify(x["title"]) for x in items)
    top = sorted(items, key=lambda x: x["views"], reverse=True)[:10]

    today = dt.date.today().isoformat()
    lines = []
    lines.append(f"# Анализ канала {data.get('uploader_id') or data.get('channel') or ''}".strip())
    lines.append("")
    lines.append(f"Дата анализа: {today} UTC  ")
    lines.append(f"Всего роликов: **{len(items)}**  ")
    lines.append(f"Период: **{items[0]['date']} → {items[-1]['date']}**")
    lines.append("")
    lines.append("## Динамика публикаций по месяцам")
    for (y, m), c in sorted(by_month.items()):
        lines.append(f"- {y}-{m:02d}: {c}")
    lines.append("")
    lines.append("## Тематическая структура (по заголовкам)")
    for k, v in by_theme.most_common():
        lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("## Топ-10 роликов по просмотрам")
    for x in top:
        lines.append(f"- {x['date']} — **{x['views']}** — {x['title']} ({x['url']})")
    lines.append("")
    lines.append("## Полная хронология (все ролики)")
    for x in items:
        lines.append(
            f"- {x['date']} | {classify(x['title'])} | {x['title']} | 👀 {x['views']} | {x['url']}"
        )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(str(out))


if __name__ == "__main__":
    main()
