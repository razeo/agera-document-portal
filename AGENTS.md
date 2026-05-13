# AGENTS

This file is for AI agents (Hermes, Claude Code, Codex) working on the AGERA Document Portal.

## Project Overview

AGERA Document Portal — Flask web application for generating legal documents (Odluka o osnivanju & Statut) for DOO (limited liability companies) in Montenegro. Generates PDFs via WeasyPrint, serves HTMX-powered frontend, integrates with AGERA wiki for up-to-date legal content.

**Primary users:** Accounting agencies, business consultants, entrepreneurs forming companies in Montenegro.

**Core value:** One-click document generation using current Montenegrin law, no legal expertise required.

## Build Commands

```bash
# Development (Flask dev server)
python -m flask run --port 5000

# Production (Gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Install dependencies
pip install -r requirements.txt

# Lint / type check (if mypy/pylint installed)
pylint app.py
```

## Architecture

- **Framework:** Flask (Python 3.12)
- **PDF Generation:** WeasyPrint (HTML → PDF)
- **Frontend:** HTMX + Tailwind CSS + Alpine.js (no build step)
- **Wiki Integration:** Reads markdown from AGERA wiki directory (mounted at `WIKI_PATH`)
- **Sessions:** UUID-based, files stored in `generated_pdfs/` (auto-cleanup)
- **Routes:** `/` (home), `/wiki` (explorer), `/wiki/<cat>/<slug>` (page), `/generate-doo` (single-member), `/generate-doo- visečlano` (multi-member), `/api/health` (monitoring)

**Data flow:** User fills form → HTML template rendered with Jinja → WeasyPrint converts to PDF → ZIP download.

**No database.** All state is in-memory/session; sources are static markdown files.

## Security Baseline

- Validate all form inputs server-side (already implemented)
- Never store or log user data beyond session lifetime
- Files in `generated_pdfs/` are temporary — deleted after response
- `.env.local` contains secrets — never commit
- Follow OWASP Top 10 (already baseline for Flask apps)
- AGERA wiki directory is read-only — path configured via `WIKI_PATH`

## Engine Guidance

- **Flask route changes, PDF template edits, wiki integration tweaks** → Hermes native (terminal + file edits)
- **New document type (Odluka za j.d.o.o, Pravilnik, etc.)** → Claude Code (complex multi-file: new template + generator + route)
- **Quick bugfix (CSS typo, form validation tweak)** → Codex
- **Deploy, monitor, schedule** → Hermes only
- **Not sure?** Tell Hermes: `run choose-engine`

## Monitoring

- Health endpoint: `GET /api/health` → `{"status": "ok", "service": "agera-document-portal", "timestamp": "..."}`
- Error tracking: Not yet configured (Sentry TBD)
- Uptime: Uptime Kuma polling `/api/health` every 60s
- Logs: Flask dev server stdout; production → Gunicorn access/error logs

## Deployment

- **Platform:** Custom VPS (currently running on Pop!_OS 24.04)
- **Process manager:** systemd or screen/tmux
- **Port:** 5000
- **Reverse proxy:** Nginx (optional, for HTTPS)
- **Production URL:** http://localhost:5000 (currently local only)
- **No CI/CD** — manual deploy via `git pull` + restart

## Commit Conventions

- One commit per meaningful change
- Never commit `.env.local` or generated PDFs
- Prefix commits: `feat:` (new feature), `fix:` (bug), `docs:` (wiki/docs), `refactor:` (no functional change)
