---
name: grafana-admin-snt
description: Configure and operate Grafana for SNT electricity analytics on this host. Use when user asks to add/edit Grafana panels, variables, filters, data sources, dashboard layout/order, access control, port/firewall restrictions, or to diagnose Grafana datasource/panel errors (for example "No data", picker not filtering, broken SQL queries).
---

# Grafana Admin (SNT)

Use this skill to make reliable, repeatable Grafana changes for SNT electricity dashboards.

## Current environment (already configured)

- Grafana service: `grafana-server`
- URL: `http://185.28.175.67:33917`
- Admin login: `tony` / `tony1pwd`
- Port: `33917/tcp`
- Firewall: allow only these source IPs:
  - `80.66.87.163`
  - `80.249.151.50`
  - `150.241.122.203`
  - `185.28.175.67`
- Main datasource for dashboard editing: `SNT Postgres Live`
- Dashboard UID: `sntchayka-electricity`
- Dashboard URL path: `/d/sntchayka-electricity/snt-chayka-electricity`
- DB: PostgreSQL `appdb`, schema `sntchayka`, table `electricity_readings`

## Fast health checks

Run:

```bash
systemctl is-active grafana-server
curl -sS -u tony:tony1pwd http://127.0.0.1:33917/api/health
curl -sS -u tony:tony1pwd http://127.0.0.1:33917/api/datasources | jq '.[].name'
```

If dashboard panels fail, test panel SQL through `/api/ds/query` before editing layout.

## Safe edit workflow (required)

1. Export current dashboard JSON:

```bash
curl -sS -u tony:tony1pwd http://127.0.0.1:33917/api/dashboards/uid/sntchayka-electricity > /tmp/snt-db.json
```

2. Edit JSON programmatically (Python + API), not manually in UI only.
3. Re-import with `overwrite=true`.
4. Re-check with `/api/ds/query` for 1-2 key panels.
5. Tell user to hard refresh if mobile cache shows stale layout.

## Panel/filter rules for this dashboard

- Panel 1 (`Потребление по каждому выбранному участку`): filter by time + selected plots.
- Panel 2 (`Суммарное потребление по выбранным участкам`): filter by time + selected plots.
- Remaining panels: filter by time range only (unless user explicitly asks otherwise).
- Default dashboard time range: `now-2y` to `now`.

## Variable (picker) rules

For plot picker, keep:

- `name`: `plot`
- `multi`: `true`
- `includeAll`: `true`
- `allValue`: `.*`
- query:

```sql
select distinct plot_no as __text, plot_no as __value
from sntchayka.electricity_readings
order by 1
```

Use picker in SQL as regex:

```sql
plot_no ~* '${plot:regex}'
```

## Common fixes

- `No data` in Stat panel:
  - return `time_series` with `now() as "time", <value> as value`.
- Datasource cannot be changed (`read-only data source`):
  - create a new editable datasource and repoint dashboard panels to its UID.
- Picker seems stuck on All:
  - reset variable definition/query/options/current and re-import dashboard.
- Layout not changing on mobile:
  - remove duplicate panels (same title different ids), then re-import.

## How to add new analytics quickly

When user asks for new chart(s):

1. Clarify filter scope (time only vs time+plot picker).
2. Add panel with stable unique `id` and explicit `gridPos`.
3. Keep units (`kwh`, `percent`, etc.) explicit in `fieldConfig`.
4. For summary KPIs, prefer Stat + single-row query.
5. For trends, prefer Time series + grouped monthly query.

## What Grafana is good for (brief)

- Real-time/near-real-time dashboards from SQL sources.
- Shared interactive filtering (time + variables).
- Fast KPI + trend + table composition on one page.
- Easy iterative updates without changing backend app code.
