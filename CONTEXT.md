# Elektrenai — CONTEXT

## Status
2026-10-13 (2nd session): map rebuilt for use — one "Sluoksniai" panel (a row per
layer, per-purpose for-sale toggles, "Planuojama plėtra" layer), "Kaip naudotis" tab,
source links everywhere, responsive on phones/tablets, installable app with a
new-version notice; installed on the user's tablet via the top-bar "Įdiegti" button
(Chrome menu install is blocked by the same-origin bug —
`wiki/frameworks/chrome-android-pwa-install-same-origin.md`). Live: v01b70a7.
The buyer's offer is out of every public file; negotiation docs are git-ignored.
Municipal plans checked: near the block only housing/commercial (189–539 m), no
industrial plan in 2026, general plan stalled since 2026-03-17.
2026-10-13 (3rd session): private lease track ready to send — agreement draft + a
clause-by-clause synthesis of the 2015 contract (PDFs in `contracts/current/`); the
user sends both to the tenant for review. Landlord details still blank.

## Next Tasks
- Private lease track — tenant has (or gets) the agreement + synthesis PDFs; record the
  reply, revise via `build_lease_proposal.py`, then fill in details + co-owner's copy;
  steps in the skill's `references/lease.md` ("Status and next step")
- Re-derive the sale counter-offer from October inputs — the June range rested on
  premises that are both gone; inputs: `wiki/elektrenai/rinkos-atnaujinimas-2026-10.md` § 5, 8
- Check 0005 every 2–4 weeks: `python C:/Users/retco/.ai-skills/elektrenai/scripts/check_0005.py`
- Monitor purpose-change requests: `C:/Users/retco/.ai-skills/elektrenai/scripts/check_requests.py`
- Skill hardening (analysis 2026-10-09): one `rebuild_map_layer.py`; checks in
  `refresh_all.py` (parsed = Found N, no 6.69 km point, bot wall); move
  `restricted_parcel.py` / `water_zones.py` to the lt-parcels skill
- More exact map boundaries: user clears aruodas's hold-button wall, then the
  skill's `scripts/fetch_coords.py` (resumes, stops on the wall)

## Key Facts
- Plot + neighbors + AZ zones → [[wiki/elektrenai/sklypas-4400-1563-8352]]
- Market scan 8km radius → [[wiki/elektrenai/rinkos-skenas-4728-apylinke]]
- BPD + planning analysis → [[wiki/elektrenai/bpd-planavimo-analize]]
- Master parcel list (21 objects) → [[wiki/elektrenai/sklypai-master-sarasas]]
- Dashboard v1 concept → [[wiki/elektrenai/dashboard-v1-koncepcija]]
- RC/geoportal API research → [[wiki/elektrenai/geoportal-lt-api-research]]
- Paskirties keitimo precedentai (16 prašymų; klasteris NEAUGO per 2026-06→08) → [[wiki/elektrenai/paskirties-keitimo-precedentai]]
- **Spalio atnaujinimas (naujausi skaičiai)** → [[wiki/elektrenai/rinkos-atnaujinimas-2026-10]]
- **Savivaldybės plėtra prie bloko (2026-10-13)** → [[wiki/elektrenai/savivaldybes-pletra-2026-10]]
- Rugpjūčio atnaujinimas → [[wiki/elektrenai/rinkos-atnaujinimas-2026-08]]
- **Realūs sandoriai + RC formulės blokui** → [[wiki/elektrenai/rc-sandoriu-duomenys-2026]]
- Private negotiation material → skill `references/lease.md` + `contracts/` (git-ignored)
- Projekto darbo eiga, monitoringas, klaidų istorija → `elektrenai` skill
  (`C:/Users/retco/.ai-skills/elektrenai/`, private ai-skills repo; scripts in `scripts/`, data stays here)

## Dead Ends
- All RC/geoportal WFS/query/geocoding APIs: 401 — do not retry
- geoportal "Duomenų paieška": no cadastre search by number
- registrucentras.lt/ntr: React SPA, no public JSON
- SŽNS zone vectors via returnGeometry=true: 401 — raster tiles + identify only
- Chrome App-Bound Encryption: cookies undecodable without admin — use CDP method
- aruodas.lt direct scrape: DataDome blocks home/hotspot IP — use CDP cookie export
- Address → parcel boundary: impossible. Listings have no house number, RC parcel
  ZIP has no address fields, Address Registry has no cadastral number (and its
  spatial API returns 0 rows). Use the listing's embedded map pin + point-in-polygon.
- `01.3-NNN` .jpg URL probing for new requests: dead since 2026-08-06 (numbering
  changed to PZNPB-K####). Fails SILENTLY — returns 0. Scrape the register page.
- `formavimo_data` in the RC ZIP = ZIP generation date, not parcel formation.
  Useless for detecting change; diff two ZIP snapshots instead.
- `geocode_listings.py` without `--google-key`: falls back to seniūnija centroid
  silently, every plot gets the same point. Check `Counter(geocode_method)`.
- `pask_tipas=995` is "other purpose", NOT road. Roads are cadastral block /7001.
- Google geocode with a key still fails silently on genitive village names: returns
  the municipality (6.69 km) as `google`. Run the skill's `scripts/regeocode_villages.py`.
- aruodas listing pages: press-and-hold bot wall since 2026-10 — needs the user,
  not the agent. List pages still scan fine via CDP.
- e-seimas PDF links return 403 to curl — download through the browser.
- BrowserOS neo `request_human_help` returned "resolved" twice with nothing done —
  re-check the page after it returns.

## Files
- `sklypas-google.html` — main interactive map
- `parcels_42/plot_7910_0001_0431.json` — plot GeoJSON
- `.env` / `gen_config.py` / `config.js` — Maps API key (git-ignored)
- `.github/workflows/deploy.yml` — Pages deploy (injects key + build version)
- `serve.py` — local no-cache server, port 8123; top bar shows the commit
- `manifest.json`, `sw.js`, `icons/` — installable app; deploy adds `version.json`
  (polled for the update notice); `icons/qr-elektrenai.png|svg` — QR to the live map
- `TYRIMO-ISVADOS.md`, `.planning/dashboard-analysis-content.md` — git-ignored
  (hold offer figures), kept on disk
- `legal/` — official law PDFs (IX-1314, XIII-2166, Civil Code) + README of articles used
- `contracts/` — private working documents (git-ignored, never committed)
- `.firecrawl/market_geo_2026-10-09.json` — 127 listings, geocoded + village fix
- `.firecrawl/listing_by_point.json` — 27 live listings resolved via August pins
- Pipeline scripts (scan, compare, map layer, zones) — in the skill's `scripts/`
- `.lt-parcels-cache/gis_pub_parcels_42_<date>.zip` — dated RC snapshots (diff baselines)
- `.lt-parcels-cache/masvert/` — RC valuation report v36 (10 files)
- `.firecrawl/bpd-tekstine-dalis.pdf` — BPD SS-070-BPL (76 pp)
- `lt-parcels/scripts/` — generic LT parcel tooling (see the skill)

## Archive

### Session 2026-10-13 (3rd) — lease synthesis document, transcription verified

- **Done:** new `-sinteze` document replaces `-argumentai`: the 2015 contract clause by
  clause (original text, status, new text struck red / green, argument, tenant's 2025
  position); agreement stays the bare list of changes. All 10 agreement clauses mapped
  (unchanged → clause 9; 2.2 "clarified", not struck). 2015 text verified against a
  Tesseract (lit) OCR word diff + zoomed read: 9 transcription errors fixed.
- **Decided / overturned:** user: synthesis is sent to the tenant with the agreement (PDF
  only); 5.1 date = 2015.09.02 per the paper original (scan looks like 03).
- **Code:** skill `scripts/build_lease_proposal.py`, `references/lease.md` (ai-skills
  commits cdbd34c..5743a57); outputs in `contracts/current/` (git-ignored).
- **Entry point:** `python C:/Users/retco/.ai-skills/elektrenai/scripts/build_lease_proposal.py contracts/current/0431-susitarimas-musu-redakcija-2026-10.docx`
- **Not measured:** tenant's reply; Tesseract-OCR left installed (`C:\Program Files\Tesseract-OCR`).

### Session 2026-10-13 (2nd)
- **Map usability**: layers panel with a row per layer + visible descriptions, groups
  reordered (restrictions second), per-purpose for-sale toggles, "Planuojama plėtra"
  layer with plan + asking price, "Kaip naudotis" tab, source links on every tab and
  every listing (aruodas URLs also kept by skill `gen_layer_v2.py`), responsive layout,
  installable app + update notice + install button, QR code. Deployed v01b70a7.
- **Research**: municipal planned development → wiki `savivaldybes-pletra-2026-10`;
  the October "200–300 m" re-parcelling was ~510 m and is a housing plan (history § 14).
- **Privacy**: buyer's offer removed from page and tracked files; three negotiation
  docs untracked + git-ignored (still in older public commits).

### Session 2026-10-13 (1st)
Private track: counter-proposal audited twice, `lt-land-lawyer` skill created.
Detail: `CONTEXT-ARCHIVE.md`.

### Session 2026-10-12
Private track: original documents audited, first counter-proposal drafted (all
private). Detail: `CONTEXT-ARCHIVE.md`.

### Session 2026-10-09
Full data refresh, map zones and dark theme, private track opened, skill moved to
the private ai-skills repo. Detail: `CONTEXT-ARCHIVE.md`.

### Session 2026-08-10
Data refresh, RC mass-valuation report mined (zone 8.16 values are modelled), map
rebuilt as a 3-view app, `elektrenai` skill created. Detail: `CONTEXT-ARCHIVE.md`.

### Sessions 2026-06-11 → 2026-06-17
Boundaries confirmed, SŽNS overlay, Rimi identified, lt-parcels skill created,
RC mass valuation read, 65 TPDRIS docs + all 16 purpose-change requests OCR'd,
scraping pipeline built (CDP solved DataDome), 119-listing scan, dashboard spec
written, and the 5-session village-name error corrected (block is **Kakliniškių
k.**, not Ausieniškių k.). Full detail: `CONTEXT-ARCHIVE.md`.
