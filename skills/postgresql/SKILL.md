---
name: postgresql
description: Work with PostgreSQL databases and structured data lifecycle (store, query, aggregate, migrate, analyze). Use when data should be structured for temporary or long-term retrieval with SQL slices/reports.
---

# postgresql

## Read first

- `/home/adam/dev/tools/q-tools/docs/vps-postgres.md`

## Default connection model

Use non-sudo SQL access as `tony_admin` for routine work.

Example:

```bash
psql "host=127.0.0.1 port=5432 dbname=appdb user=tony_admin sslmode=disable"
```

## When to use this skill

- Need durable structured storage instead of ad-hoc text files
- Need repeatable queries/slices/aggregations
- Need staging tables for intermediate computations
- Need joins/filters/grouping for reporting

## Rules

1. Treat PostgreSQL as first-class workspace resource.
2. Prefer direct non-sudo SQL operations.
3. Ask confirmation before destructive SQL (DROP/TRUNCATE/mass DELETE).
4. Keep secrets/passwords out of replies/logs.
5. Use sudo only for system-level DB operations (service/config/firewall/packages).
