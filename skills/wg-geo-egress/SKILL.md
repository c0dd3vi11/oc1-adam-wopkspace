---
name: wg-geo-egress
description: Use WireGuard regional egress profiles on this host to run network requests from a different IP/region (DE/RU/US), quickly diagnose tunnel failures, and choose fallback region. Trigger when user asks to run/check requests from another geo, test "other IP", verify region-specific access, or debug WireGuard connectivity.
---

# WG Geo Egress

Use this skill to run requests through specific WireGuard regions and to debug failures fast.

## Profiles on this host

- `wgge1` → DE (Frankfurt), egress IP `80.66.87.163`
- `wgmsk1` → RU (Moscow), egress IP `80.249.151.50`
- `wgusa1` → US (Dallas), egress IP `150.241.122.203`

## Fast usage

- Get region/IP for a profile:
  - `wg-ipinfo wgge1`
  - `wg-ipinfo wgmsk1`
  - `wg-ipinfo wgusa1`
- Run any request through profile interface:
  - `wg-curl <iface> <url> [curl args...]`
  - example: `wg-curl wgusa1 https://ipinfo.io/json`

## Health checks

1. Interface service state:
   - `systemctl status wg-quick@<iface>`
2. WireGuard handshake/traffic:
   - `wg show <iface>`
3. End-to-end geo check:
   - `wg-ipinfo <iface>`

## Failure triage

If `transfer: 0 B received` and no `latest handshake`:

1. Check server UDP port allowlist/firewall.
2. Verify peer keys on both sides.
3. Verify endpoint DNS/IP and port.
4. Restart interface:
   - `sudo systemctl restart wg-quick@<iface>`

If handshake exists but HTTP request fails:

1. Check server NAT/forwarding.
2. Check remote egress restrictions.
3. Retry with another profile (`wgge1`/`wgusa1`) as fallback.

## Auto-start expectation

Interfaces should be enabled at boot:

- `wg-quick@wgge1`
- `wg-quick@wgmsk1`
- `wg-quick@wgusa1`

Re-enable if needed:

- `sudo systemctl enable wg-quick@<iface>`
