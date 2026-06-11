# Elektrenai — project rules

**Read `CONTEXT.md` first — it is the source of truth** (plot data, findings, map/UI state,
dead ends, next tasks). `DECISIONS.md` holds the decision log. Do not duplicate their
content here.

## Hard rules

- **Maps API key: NEVER inline in code or commits.** Local dev: `python gen_config.py`
  (writes git-ignored `config.js` from `.env`). Production: GitHub Actions injects from
  the `MAPS_API_KEY` repo secret. An inline key already caused a secret-scanning incident
  (key rotation + history rewrite).
- **`file://` does not work** (RefererNotAllowedMapError). Test via
  `python -m http.server 8123` + Playwright screenshots before deploying.
- **Deploy = commit + push to `main`.** GitHub Pages workflow runs automatically;
  verify with `gh run watch`. Live: https://gerimantas.github.io/elektrenai/
- **RC/geoportal APIs: do not retry the dead ends** listed in CONTEXT.md ("Dead Ends" +
  "SŽNS Overlay" sections). Parcel geometry comes from the data.gov.lt municipality ZIP;
  SŽNS zone vectors are blocked (401) — only raster tiles + `identify` attributes work.
- **`.firecrawl/` is git-ignored** — working scripts, scraped data, computed zone JSONs
  live there. Reuse `parcels_42.zip` and the analysis scripts instead of re-downloading.
