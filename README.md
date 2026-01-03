# Realm of Warriors Sheet Embed

Brief notes on the character sheet embed, file layout, and common commands for this deployment.

## Project layout (workspace root)
- `backend/templates/characters/sheet_embed.html` — Django template that renders the multi-page sheet.
- `js/sheet_embed.js` — Front-end logic that fills the sheet from the JSON payload provided by the view.
- `blank_sheet.css` — Shared stylesheet for all pages of the sheet.
- `images/` — Corner art, logos, QR placeholder, etc.
- `staticfiles/` — Collected static output (target of `collectstatic`).
- `index.html` — Static reference version of the sheet (not Django-templated) for quick visual checks.

## How rendering works
1) Django view injects serialized character data as `data_json` plus fallback fields (character code/name/player/profession).
2) `sheet_embed.html` places those into `window.sheetData`/`window.sheetFallback` and loads `js/sheet_embed.js`.
3) `sheet_embed.js` populates all `[data-field]` and list tables (features, talents, proficiencies, languages, spells, inventory, overflow pages, notes).
4) Overflow handling: features/talents are truncated to visible rows and long/extra items flow to the definitions tables on Page 3; notes have a dedicated Page 4.

## Common commands (from `/var/www/forge.realmofwarriors.games/public_html`)
Activate venv (needed for all Python commands):
```
source .venv/bin/activate
```

Collect static assets after template/JS/CSS changes:
```
cd backend && ../.venv/bin/python manage.py collectstatic --no-input
```

Run gunicorn (foreground) for the Django site:
```
cd backend && ../.venv/bin/gunicorn rowsite.wsgi:application --bind 127.0.0.1:8000
```
Stop a foreground gunicorn: Ctrl+C in that terminal.

Check if gunicorn is running:
```
pgrep -af gunicorn
```

## Deployment / serving notes
- Gunicorn is currently started manually (foreground). If you want a managed service, create a systemd unit or supervisor config that runs `../.venv/bin/gunicorn rowsite.wsgi:application --bind 127.0.0.1:8000` from `/var/www/forge.realmofwarriors.games/public_html/backend` and set `User=jeric` (or appropriate user).
- Static files are served from `staticfiles/`; be sure your web server (e.g., nginx) points to that directory for `/static/` and `/images/` if proxying.
- Add cache-busting on `js/sheet_embed.js` if browsers are sticky (e.g., `<script src="/js/sheet_embed.js?v=YYYYMMDDHHMM"></script>` in the template).

## Endpoints / URLs
- Gunicorn bind: http://127.0.0.1:8000
- Root `/` may 404 if not routed; use the Django view that renders the sheet embed (character-specific endpoint).

## Editing notes
- Keep JS logic in `js/sheet_embed.js`; only bootstrapping stays inline in the template.
- When adding new data fields, add `data-field` targets in the template and map them in `sheet_embed.js`.
- Run `collectstatic` and restart gunicorn after front-end changes so the static bundle is updated.

## Troubleshooting
- 404 at `/`: The root URL may not be routed; hit the embed endpoint or Django views directly.
- Worker timeout with no URI: usually a stray connection; worker restarts automatically when run in foreground.

## License/attribution
- Page footer credits: © 2026 MagiTomes LLC. Copying is permitted for personal use.
