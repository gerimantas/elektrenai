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

## Market Value (researched 2026-06-11)

**Official RC mass valuation (our plot 4400-1563-8352): 5 880 €** (valuation date 2026-01-01) ≈ 3 510 €/ha.
Source: registrucentras.lt/masvert/paieska-obj (public, queried by unique number; POST with CSRF token).
Mass valuation is fiscal — typically 2–4× below real market.

**Listing market, agricultural plots in Elektrėnų sav.** (kampas.lt + alio.lt, 2026-06; aruodas.lt blocks bots):

| Location | Area | Price | €/ha |
|---|---|---|---|
| Karkučių k. | 4.82 ha | 39 000 € | 8 084 |
| Stančikų k. | 2.68 ha | 25 000 € | 9 328 |
| Žuvyčių k. (mixed) | 7.99 ha | 80 000 € | 10 013 |
| Kurkliškių k. | 2.65 ha | 48 000 € | 18 144 |
| Semeliškių k. (pond) | 16.34 ha | 299 900 € | 18 357 |
| Semeliškės (kaimo plėtra) | 1.65 ha | 69 500 € | 42 121 |

Typical agri land in the municipality: **~8 000–18 000 €/ha**.

**Local anomalies (near our plot):**
- Kakliniškės, 3.05 ha agri next to A1: 299 000 € (98 000 €/ha) — speculative, highway adjacency
- **Ausieniškės, Gėlių g., 3 ha INDUSTRIAL: 390 000 € (130 000 €/ha)** — same village as our plot; confirms industrial trend (plus 0005 purpose change 443 m away)

**Our plot estimate (1.675 ha, agri):**
- As agricultural land now: **~13 000–30 000 €** (8–18 k€/ha; narrow strip + gas pipeline AZ push toward lower end)
- RC fiscal value 5 880 € = floor
- Speculative upside: if Ausieniškės industrial zone spreads, purpose change could lift toward 100–130 k€/ha — but pipeline AZ limits buildable area, Ambergrid approval needed

Raw data: `.firecrawl/kampas-sklypai.md`, `.firecrawl/alio-sklypai.md`, `.firecrawl/rc-masvert-result.html`.

## Geometry Verification (vs official RC map)

Compared our polygon to RC PDF map (geoportal.lt, M 1:2000, 2026-06-03):
- Boundaries/shape: ✅ identical (same RC source)
- Area from our coords (shoelace) = 1.6750 ha = RC declared → **0.00% diff**
- Proportions correct in Google Maps (Web Mercator, conformal, <0.1% distortion at this scale; tilt=0 enforced)
- **Difference:** RC map shows SŽNS layers — now ADDED as a togglable raster overlay (see below).

## SŽNS Overlay (DONE 2026-06-11)

Togglable raster overlay of RC special land-use conditions, live on the map.

- **Source:** geoportal.lt `rc_szns/MapServer` cache. Published in **LKS94 (EPSG:3346)**, not Web Mercator → can't use a plain Google ImageMapType.
- **Method:** custom `OverlayView` + **proj4** (CDN). Fetches native LKS94 cache tiles, positions each by projecting its corners LKS94→WGS84. LOD auto-picked per Google zoom (9–12; zoom 18 → finest 0.26 m/px). Empty tiles 404 → hidden.
- **API limit:** `returnGeometry=true` is **401 (blocked)** — RC won't serve SŽNS polygons (GDPR/cache protection, same as owner names). So vector zones are impossible; raster tiles are the only way to show real boundaries. Attributes (which zones cross) DO work via `identify` with `returnGeometry=false`.
- **Zones crossing plot 7910/0001:0431** (11 objects, 4 types): Magistralinių dujotiekių AZ (107, Ambergrid) ×6, dujotiekių vietovių klasės (171) ×3, Elektros tinklų AZ (106) ×1, **Kultūros paveldo objektų AZ (119) ×1 — new finding**.
- Verified in-browser (Playwright): pixel-aligned at zoom 18 (pipeline corridor matches plot long axis).

## Dashboard "Tyrimas" Tab (2026-06-11)

Info panel has two tabs: **Legenda** (layers/SŽNS) and **Tyrimas** (research findings):
purpose changes nearby, market prices, road-access analysis.

**Merged block (2026-06-11):** map shows 0429+0430+0431 as one unit — red outline with
total area label (**5.0250 ha**, shapely union of RC parcels), strips kept as yellow
inner division lines with their own Nr/area labels. Orange polyline marks the combined
road-4728 frontage: **51.9 m** (0429 ~35 m + 0430 ~16.8 m; 0431 doesn't reach the road —
0050 in between).

**Access verdict (merged):** 51.9 m frontage fits a 7 m two-way truck entrance with full
R 12.5 m turning arcs inside the plot, plus room for a second entrance or waiting pocket;
12×12 m turning pad fits right at the entrance. Requires connection conditions from
VĮ "Via Lietuva" (state regional road) + Ambergrid approval if pipeline AZ crosses the
entrance. Comfortable margin — well above the ≥20 m comfort norm.

Neighbors of 0430 (RC open data): 0429 (NW twin strip, 423 m), 0431, 0050, 0023,
0031 (N tip), 7910/7001:0009 (road parcel 4728, pask 995).

## No-Build Zones in Merged Block (2026-06-11)

Map shows hatched red no-build AZ zones inside the merged block (toggle in legend):

- **Restricted: 1.2250 ha (24.4%)** of 5.0250 ha — pipeline AZ 1.0973 ha (25 m each side
  of both Minskas–Kaliningradas and GIPL axes, crossing the north part), road-4728 AZ
  0.1133 ha (20 m beyond road parcel), heritage AZ ~0.02 ha (corner)
- **Usable for buildings/logistics: ~3.80 ha (75.6%)**
- Method: RC blocks zone vectors (401) → zones reconstructed from statutory widths
  (SŽNS law) + OSM axes; heritage 119 digitized from RC raster (yellow pixels).
  Verified visually against RC raster corridor — pixel-aligned. Script:
  `.firecrawl/restricted_zones.py`, data `.firecrawl/restricted.json`
- Caveats: whole strip is in pipeline location-class territory (171) — design
  constraints, not a ban; 110 kV line passes 47 m away (its AZ misses the block);
  in AZ paved yards/roads allowed with Ambergrid/road-owner approval

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

1. Optionally show plot 7910/0008:0037 too
2. Update Obsidian wiki: mark data.gov.lt method as ✅ WORKS in geoportal-lt-api-research.md
