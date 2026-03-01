# Deploy and debug notes for web-adam

## Deploy commands

```bash
cd /home/adam/dev/tools/www-adam
uv run pytest
uv run ruff check .
sudo systemctl restart webadam
sudo systemctl is-active webadam caddy
```

## Check routes/templates

```bash
grep -n "@app.get(\|@app.post(" app/main.py
ls -1 app/templates
```

## Runtime logs

```bash
sudo journalctl -u webadam -n 120 --no-pager
sudo journalctl -u caddy -n 120 --no-pager
```

## Auth paths

- App login page: `/login`
- Telegram callback: `/auth/telegram`

## Public checks

```bash
curl -I https://185.28.175.67.sslip.io/
curl -I https://185.28.175.67.sslip.io/login
```
