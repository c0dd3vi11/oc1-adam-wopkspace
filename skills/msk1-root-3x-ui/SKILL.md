---
name: msk1-root-3x-ui
description: Work with the msk1 VPS over SSH as root and account for installed 3x-ui panel. Use when user asks to connect/check/configure msk1, run commands on msk1, troubleshoot server state, or do any 3x-ui related operations on msk1.
---

# msk1 root + 3x-ui

Use this skill for any task on the `msk1` VPS.

## Connection profile

- Host alias: `msk1`
- Host/IP: `80.249.151.50`
- User: `root`
- Key: `~/.ssh/msk1_ed25519`
- SSH config entry exists in `~/.ssh/config`

## Mandatory precheck

Run a quick identity check before making changes:

```bash
ssh msk1 'hostname && id -un'
```

Expected user is `root`.

## Execution rules

1. Use `ssh msk1 '<command>'` for one-off tasks.
2. For multi-step changes, group commands into one remote shell block to reduce reconnection overhead.
3. Treat destructive operations carefully and ask for confirmation first.
4. Remember that `3x-ui` is installed on this host; check service/panel state before changing related networking/proxy settings.

## Useful checks

```bash
ssh msk1 'uname -a && uptime'
ssh msk1 'systemctl status 3x-ui --no-pager || true'
ssh msk1 'ss -tulpen | head -n 30'
```
