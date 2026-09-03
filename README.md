# nki-nucleate-india

## What this is

A pipeline in four stages:

1. **Scrape** — per-source scrapers under `scraper/`, driven by `master.py`.
2. **Transform** — dedupe and normalize the raw records (`transform/`).
3. **Store** — write the curated records to Supabase (schema in `supabase/migrations/`).
4. **Serve** — a search API over the curated data (`api/`).

A map-of-India frontend comes later, as a separate effort. Not in this repo yet.

## Local setup

```bash
git clone <repo-url> && cd guitar
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env           # then fill in your Supabase keys
```

## Running

```bash
python master.py
```

`data/raw/` and `data/processed/` are local scratch dirs for development and are gitignored.

## Supabase

Row Level Security (RLS) policies must be enabled on any Supabase table before it is exposed to a frontend.

