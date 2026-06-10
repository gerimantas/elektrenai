# Elektrenai — CONTEXT

## Project Goal
Research and document land plot Nr. 4400-1563-8352 (cadastral 7910/0001:0431) in Ausieniškių k., Elektrėnų sav. Extract cadastral boundaries, coordinates, and protection-zone data from Lithuanian geospatial services.

## Status

✅ **SOLVED** — exact parcel boundary + coordinates obtained from RC open data (data.gov.lt). Vector geometry verified visually against geoportal NTR render (perfect alignment).

## Key Findings

- Plot 4400-1563-8352 = kadastrinis Nr. 7910/0001:0431
- **Location: Ausieniškių k., Elektrėnų sen.** (NOT Kakliniškės — old docs were wrong)
- **Area: 1.6750 ha**, purpose type 610 (agricultural), formed 2008-05-07
- **Centroid (LKS94/EPSG:3346): 543874, 6073258**
- Bbox: 543753, 6073004 → 543910, 6073352 (~157 m × ~348 m, long narrow strip / old field rėžis)
- In Ambergrid magistralinių dujotiekių apsaugos zona (table 3, row 164) — any construction needs Ambergrid approval
- Web research: NO active planning docs/permits for this plot (2024–2026). Clean.

## Files

- `sklypai.md` — main data file: metadata, coordinates, map links, API sources
- `parcels_42/plot_7910_0001_0431.json` — exact GeoJSON geometry (extracted from RC dataset)
- `nuotraukos/plot-ntr-exact.png` — clean NTR cadastral map (geoportal mapproxy export)
- `nuotraukos/plot-highlight.png` — parcel highlighted (blue outline + red fill) on NTR map
- `.firecrawl/ambergrid.md` — scraped Ambergrid protection zone data
- `.firecrawl/rc-mapserver-info.json` — geoportal MapServer layer reference
- `find_plot6.py` — working geoportal Playwright login (kept for reference)
- `scrape_plot.js` — regia.lt automation (kept for reference)

## The Winning Method — RC Open Data (data.gov.lt)

After 12 failed API approaches (all auth-gated), the public download dataset solved it:

1. data.gov.lt dataset 2831 "Kadastriniai žemės sklypai. Erdviniai duomenys" (RC, CC BY 4.0, monthly)
2. Per-municipality ZIP: `https://www.registrucentras.lt/aduomenys/?byla=gis_pub_parcels_42.zip` (42 = Elektrėnų sav.)
3. GeoJSON inside (EPSG:3346), 24,123 parcels → filter by `kadastro_nr` field
4. No auth, no rate limit. This is the canonical source for any LT parcel boundary.

## Dead Ends (DO NOT RETRY)

Full log: `wiki/elektrenai/geoportal-lt-api-research.md`. Summary:
- All RC/geoportal query/WFS/geocoding APIs require auth (401)
- geoportal "Duomenų paieška" UI has no cadastre search by number
- registrucentras.lt/ntr is React SPA, no public JSON
- Old bbox in docs (lon 24.840–24.917) pointed to Kazokiškės — wrong area

## Next Session Tasks (optional)

1. Overlay parcel polygon on ESRI ortofoto (satellite) at exact bbox → see actual land use (forest/field/structures)
2. Update Obsidian wiki: mark data.gov.lt method as ✅ WORKS in geoportal-lt-api-research.md
3. Check neighbors / Ambergrid pipeline exact path across the parcel
