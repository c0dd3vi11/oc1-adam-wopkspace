#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path
import urllib.parse
import urllib.request


def call_api(token: str, method: str, params: dict) -> dict:
    url = f"https://api.telegram.org/bot{token}/{method}?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def _read_token_from_secrets_file(path: Path) -> str:
    if not path.exists():
        return ""
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k.strip() in {
            "TELEGRAM_BOT_TOKEN",
            "TELEGRAM_BOT_TOKEN_SWARMPRIMEBOT",
            "TELEGRAM_BOT_TOKEN_LOSTFILMDOTTVBOT",
        }:
            token = v.strip()
            if token:
                return token
    return ""


def resolve_token() -> str:
    # 1) Prefer runtime env
    for key in (
        "TELEGRAM_BOT_TOKEN",
        "TELEGRAM_BOT_TOKEN_SWARMPRIMEBOT",
        "TELEGRAM_BOT_TOKEN_LOSTFILMDOTTVBOT",
    ):
        v = os.environ.get(key, "").strip()
        if v:
            return v

    # 2) Fallback to q-tools secrets file (local setup)
    token = _read_token_from_secrets_file(Path("/home/adam/.config/q-tools/secrets.env"))
    if token:
        return token

    raise RuntimeError(
        "Telegram bot token not found (env or /home/adam/.config/q-tools/secrets.env)"
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Edit Telegram forum topic (name/icon)")
    p.add_argument("--chat-id", required=True)
    p.add_argument("--thread-id", required=True, type=int)
    p.add_argument("--name", required=True)
    p.add_argument("--icon-custom-emoji-id", required=True)
    p.add_argument("--list-icons", action="store_true")
    args = p.parse_args()

    token = resolve_token()

    if args.list_icons:
        data = call_api(token, "getForumTopicIconStickers", {})
        print(json.dumps(data, ensure_ascii=False))
        return 0

    icon_id = args.icon_custom_emoji_id.strip()
    if not icon_id:
        raise RuntimeError("--icon-custom-emoji-id must be non-empty")

    params = {
        "chat_id": args.chat_id,
        "message_thread_id": args.thread_id,
        "name": args.name,
        "icon_custom_emoji_id": icon_id,
    }

    data = call_api(token, "editForumTopic", params)
    print(json.dumps(data, ensure_ascii=False))
    if not data.get("ok"):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
