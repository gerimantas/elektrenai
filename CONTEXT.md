# Elektrenai — CONTEXT

## Project Goal
Research and document land plot Nr. 4400-1563-8352 (cadastral 7910/0001:0431) in Ausieniškių k., Elektrėnų sav. Map parcel boundaries, neighbors, and nearby planning activity. Published as an interactive Google Maps page on GitHub Pages.

## Status

✅ **DONE** — exact boundaries from RC open data, verified against official RC map (0.00% area diff). Interactive map deployed to GitHub Pages with our plot + 6 neighbors + a purpose-change plot.

**Live:** https://gerimantas.github.io/elektrenai/

## Key Findings

- Plot 4400-1563-8352 = kadastrinis Nr. 7910/0001:0431
- **Location: Ausieniškių k., Elektrėnų sen.** (RC). Google reverse-geocodes the spot as "Kakliniškės" — same area, different naming systems. Old docs saying only "Kakliniškės" were incomplete.
- **Area: 1.6750 ha**, purpose type 610 (agricultural), formed 2008-05-07
- **Centroid (LKS94/EPSG:3346): 543874, 6073258** | WGS84: 54.793655, 24.682243
- Real dimensions: 157.6 m × 348.0 m, long narrow strip (old field rėžis), 9 vertices
- In Ambergrid magistralinių dujotiekių apsaugos zona (table 3, row 164) — construction needs Ambergrid approval
- Web research: NO active planning docs/permits for this plot (2024–2026). Clean.

## Neighbors (6, touching — shapely geometric test, dist 0.00 m)

| Cadastral | Area | Direction | Shared border |
|---|---|---|---|
| 7910/0001:0430 | 1.6750 ha | SW (V) | 364 m |
| 7910/0001:0949 | 1.2266 ha | NE | 230 m |
| 7910/0001:0050 | 3.0500 ha | S | 130 m |
| 7910/0001:0023 | 3.1300 ha | N | 60 m |
| 7910/0001:0048 | 9.6755 ha | E | 3 m (corner) |
| 7910/0001:1014 | 2.0734 ha | NE | 2 m (corner) |

All purpose type 610. None has a purpose change.

## Nearby Purpose Change

- **7910/0001:0005** — Sabališkių k., ~443 m SW of our plot (NOT a direct neighbor).
  Agri → industrial/storage (warehouse, non-hazardous goods). App 2026-05-27 (reg. 01.3-192),
  public review until 2026-06-15. Doc: planuojustatau.lt/sites/default/files/01.3-192.jpg
- Also seen: 7910/0008:0037 (Kakliniškių k., Vakario g.) — hobby garden → residential, 0.0669 ha.

## Geometry Verification (vs official RC map)

Compared our polygon to RC PDF map (geoportal.lt, M 1:2000, 2026-06-03):
- Boundaries/shape: ✅ identical (same RC source)
- Area from our coords (shoelace) = 1.6750 ha = RC declared → **0.00% diff**
- Proportions correct in Google Maps (Web Mercator, conformal, <0.1% distortion at this scale; tilt=0 enforced)
- **Difference:** RC map shows SŽNS layers (protection zones: pipeline/road/utility hatching crossing the plot) — NOT yet on our map. Geometry is exact; only the restrictions overlay is missing.

## Files

- `sklypas-google.html` — interactive map (our plot + neighbors + change plot, labels, collapsible info)
- `index.html` — Pages entry point; CI-generated from sklypas-google.html (git-ignored)
- `parcels_42/plot_7910_0001_0431.json` — our plot GeoJSON geometry
- `parcels_42/plot_7910_0001_0005.json` — purpose-change plot geometry
- `nuotraukos/plot-ntr-exact.png` — clean NTR cadastral map
- `nuotraukos/plot-highlight.png` — parcel highlighted on NTR map
- `nuotraukos/plot-truescale.png` — polygon in true metric scale (proportion proof)
- `map_..._Ausieniškės.pdf` — official RC reference map (geoportal export)
- `.env` / `.env.example` / `gen_config.py` / `config.js` — local Maps key handling (secrets git-ignored)
- `.github/workflows/deploy.yml` — Pages deploy, injects Maps key from repo secret
- `.firecrawl/ambergrid.md`, `.firecrawl/rc-mapserver-info.json` — reference data
- `find_plot6.py`, `scrape_plot.js` — kept for reference (geoportal login / regia)

## The Winning Method — RC Open Data (data.gov.lt)

After 12 failed API approaches (all auth-gated), the public download dataset solved it:

1. data.gov.lt dataset 2831 "Kadastriniai žemės sklypai. Erdviniai duomenys" (RC, CC BY 4.0, monthly)
2. Per-municipality ZIP: `https://www.registrucentras.lt/aduomenys/?byla=gis_pub_parcels_42.zip` (42 = Elektrėnų sav.)
3. GeoJSON inside (EPSG:3346), 24,123 parcels → filter by `kadastro_nr` field
4. No auth, no rate limit. Canonical source for any LT parcel boundary.

**Owner names are NOT available** — personal data (GDPR), not in open data. Only via paid RC NTR extract.

## Google Maps + GitHub Pages Deploy

- Static HTML on GitHub Pages, key injected at deploy by Actions from `MAPS_API_KEY` repo secret.
- Key is referrer-locked (Cloud Console: gerimantas.github.io + localhost) + Maps JavaScript API.
- `file://` does NOT work (RefererNotAllowedMapError) — use the live URL or `python -m http.server`.
- Google Static Maps satellite is BLOCKED in EEA region; only JS Maps API works for satellite here.
- **Incident:** an inline key was briefly committed → GitHub secret-scanning alert. Fixed: rotated key,
  moved to Actions injection, rewrote git history (force push), alert resolved/revoked.

## Dead Ends (DO NOT RETRY)

Full log: `wiki/elektrenai/geoportal-lt-api-research.md`. Summary:
- All RC/geoportal query/WFS/geocoding APIs require auth (401)
- geoportal "Duomenų paieška" UI has no cadastre search by number
- registrucentras.lt/ntr is React SPA, no public JSON
- Old bbox in docs (lon 24.840–24.917) pointed to Kazokiškės — wrong area

## Next Session Tasks (optional)

1. Add SŽNS (special land-use conditions) overlay — geoportal has a public SŽNS mapproxy layer; show protection zones crossing the plot
2. Optionally show plot 7910/0008:0037 too
3. Update Obsidian wiki: mark data.gov.lt method as ✅ WORKS in geoportal-lt-api-research.md
