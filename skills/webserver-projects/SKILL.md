---
name: webserver-projects
description: Manage the private web project hub at /home/adam/dev/tools/www-adam (web-adam): add new mini-project pages, edit existing ones, troubleshoot auth/routing/deploy, and verify availability. Use when the user mentions "webserver", "web-adam", adding a new game/tool to the site, checking existing projects/routes, or deploying/fixing the website.
---

# Webserver Projects

Manage the web hub as a product surface, not just files: detect what already exists, implement pages/routes, deploy, and verify from the running server.

## Ground truth locations

- Project repo: `/home/adam/dev/tools/www-adam`
- Runtime env: `~/.config/web-adam/env`
- Service: `webadam` (systemd)
- Reverse proxy/TLS: `caddy`
- Public host: `185.28.175.67.sslip.io`

## Fast workflow

1. Inspect current site state:
   - `app/main.py` routes
   - `app/templates/*.html`
   - `app/templates/index.html` project list
2. Add or update project:
   - Add route in `app/main.py`
   - Add template in `app/templates/`
   - Add card/link on index page
3. Validate + deploy:
   - `uv run pytest`
   - `uv run ruff check .`
   - `sudo systemctl restart webadam`
4. Commit + push (mandatory after every completed change set):
   - `git add -A && git commit -m "..."`
   - `git push`
5. Verify runtime:
   - `sudo systemctl is-active webadam caddy`
   - `curl -I https://185.28.175.67.sslip.io/`

## Existing auth model (important)

- Site entry is guarded by Caddy.
- Telegram Login is used in app (`/login` -> `/auth/telegram`) with allowed Telegram IDs.
- Do not reintroduce Google OAuth unless explicitly requested.

## Add-new-project checklist

- Keep mobile UX first (touch controls, large hit targets).
- Keep each project self-contained in one template unless complexity requires JS split.
- Ensure project appears on index page with short description.
- Avoid breaking auth flow; all project routes must respect `_authorized` checks.

## Find existing project quickly

- Routes: inspect `app/main.py`
- Project list: inspect the `projects = [...]` block in `index()`
- Templates: list `app/templates/*.html`

## References

If needed, read: `references/deploy-and-debug.md`
