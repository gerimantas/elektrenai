# Elektrenai — CONTEXT

## Status
2026-10-12: private negotiation track advanced — the counter-proposal document is
drafted and waits for the user's review; details only in the private skill
(`references/lease.md`) and the git-ignored `contracts/` (this repo is public).
Market state unchanged since the 2026-10-09 refresh (Rimi OPERATING ~300 staff;
0005 undecided ~4 months; no industrial request within 11 km; analogue asks flat).
Map live with dark theme, water zones and 0432 zones. All pushed.

## Next Tasks
- Private negotiation track — next step and open questions in the skill's
  `references/lease.md` and `contracts/` (not in this public repo)
- Re-derive the sale counter-offer from October inputs — the June range rested on
  premises that are both gone; inputs: `wiki/elektrenai/rinkos-atnaujinimas-2026-10.md` § 5, 8
- Check 0005 every 2–4 weeks: `python C:/Users/retco/.ai-skills/elektrenai/scripts/check_0005.py`
- Monitor purpose-change requests: `C:/Users/retco/.ai-skills/elektrenai/scripts/check_requests.py`
- Find out what is planned on re-parcelled 7930/0002:0730–0733 (0.2–0.3 km S)
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

### Session 2026-10-12 (this)
- **Private negotiation track** — original documents audited and a counter-proposal
  drafted; all of it in the git-ignored `contracts/` and the skill's
  `references/lease.md` (generator: skill `scripts/build_lease_proposal.py`).
  Nothing about it belongs in this public repo.

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
