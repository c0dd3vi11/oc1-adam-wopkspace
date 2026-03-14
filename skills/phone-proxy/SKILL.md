---
name: phone-proxy
description: Use Anton's phone (Termux) as temporary outbound proxy for requests from this host via SSH reverse SOCKS tunnel on 127.0.0.1:1081. Use when user asks "сделай запрос через мой девайс", "используй прокси через мой телефон", "проверь через мой телефон" or equivalent.
---

# Phone Proxy (Termux → OpenClaw host)

Use this workflow to route host requests through Anton's phone.

## Expected phone-side setup

Assume Anton starts tunnel from Termux with:

```bash
ssh -NT \
  -p 18754 \
  -o ExitOnForwardFailure=yes \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -R 1081 \
  adam@185.28.175.67
```

Equivalent via `~/.ssh/config` host `oc1` (port `18754`) is valid.

## Verify tunnel on host

Run:

```bash
ss -ltnp | awk 'NR==1 || /:1081\b/'
curl -sS --max-time 12 --socks5-hostname 127.0.0.1:1081 https://api.ipify.org && echo
```

Interpretation:
- Success: `curl` returns external IP (phone egress region).
- Failure `Connection refused`: tunnel is not up.
- Failure `Unable to receive initial SOCKS5 response`: wrong `-R` mode (usually `-R 1081:localhost:1080` without local SOCKS server).

## Make proxied requests

For one-off HTTP(S) calls:

```bash
curl --socks5-hostname 127.0.0.1:1081 <URL>
```

For tool/CLI commands supporting proxy env:

```bash
export ALL_PROXY=socks5h://127.0.0.1:1081
```

Prefer `socks5h`/`--socks5-hostname` to keep DNS resolution on phone side.

## Fast troubleshooting checklist

1. Confirm SSH port reachable on host: `185.28.175.67:18754`.
2. Confirm tunnel process is still running in Termux.
3. Ensure phone command uses `-R 1081` (not `-R 1081:localhost:1080`, unless local SOCKS exists).
4. Re-run `curl --socks5-hostname ... ipify` from host and report resulting IP.

## Response pattern to user

Always report:
- whether proxy is up,
- observed egress IP,
- exact next action if broken (what to run in Termux).