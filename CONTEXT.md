# Elektrenai — CONTEXT

## Status
Full data refresh 2026-10-09. Nothing decisive moved: Rimi is OPERATING but with
~300 staff (800 = long-term); 0005 still undecided (~4 months); 15 new requests,
none industrial within 11 km; same analogue listings flat — the 3–8 ha median
jump (5 952 → 10 484 €/ha) is listing turnover. Five silent failures found and
fixed (town plots dropped, Google municipality fallback, aruodas bot wall,
self-overwriting diff, baseline rotation). Map listings layer rebuilt (126
listings, 22 exact boundaries). Committed locally, NOT pushed to Pages.

## Next Tasks
- Push the 2026-10-09 refresh to Pages after the user reviews it on localhost
  (`python gen_config.py && python -m http.server 8123`)
- Re-derive the counter-offer from October inputs — the June range (16–18 k€/ha)
  rested on premises that are both gone; inputs: `wiki/elektrenai/rinkos-atnaujinimas-2026-10.md` § 5, 8
- More exact map boundaries need the user to clear aruodas's press-and-hold wall in
  Chrome, then `python .lt-parcels-cache/fetch_coords.py` (resumes, stops on the wall)
- Check 0005 outcome every 2–4 weeks: `python C:/Users/retco/.ai-skills/elektrenai/scripts/check_0005.py`
- Find out what is planned on the re-parcelled 7930/0002:0730–0733 (0.2–0.3 km S)
- Monitor new purpose-change requests via the register page (the `.jpg` probe is
  dead — numbering changed to PZNPB-K####): `C:/Users/retco/.ai-skills/elektrenai/scripts/check_requests.py`

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

## Files
- `sklypas-google.html` — main interactive map
- `parcels_42/plot_7910_0001_0431.json` — plot GeoJSON
- `.env` / `gen_config.py` / `config.js` — Maps API key (git-ignored)
- `.github/workflows/deploy.yml` — Pages deploy
- `.firecrawl/market_geo_2026-10-09.json` — 127 listings, geocoded + village fix
- `.firecrawl/listing_by_point.json` — 27 live listings resolved via August pins
- Pipeline scripts (scan, compare, map layer, zones) — in the skill's `scripts/`
- `.lt-parcels-cache/gis_pub_parcels_42_<date>.zip` — dated RC snapshots (diff baselines)
- `.firecrawl/rc_model_calc.py` — RC 2026 formulas applied to the block
- `.lt-parcels-cache/masvert/` — RC valuation report v36 (10 files)
- `.firecrawl/bpd-tekstine-dalis.pdf` — BPD SS-070-BPL (76 pp)
- `lt-parcels/scripts/` — generic LT parcel tooling (see the skill)

## Archive

### Session 2026-08-10 (this)
- **Full data refresh after 8 weeks.** Rimi centre BUILT (April 2026, 42 000 m²
  not 31 000); 0005 undecided 2.5 months; cluster gained 0 new members (7 new
  requests, nearest 4.62 km, none industrial); market down 9–45 %, 14 of 84
  listings cut price. Base rate: 1 purpose change municipality-wide in 8 weeks.
- **RC mass-valuation report mined** — zone 8.16 has too few transactions, its
  figures are MODELLED (Kprikl 1.63), not transaction-based; earlier documents
  mislabelled them. Zone 8.16 holds 82 industrial plots, most of all 26 zones.
  RC formulas applied to the block: purpose change = ×13–19 fiscal value.
- **Map rebuilt** as a 3-view app: 53 listings resolved to real RC boundaries via
  their embedded map pin (address cannot do this), sortable/filterable Rinka
  table, Tyrimas as a full-window dated document.
- `elektrenai` skill created; `lt-parcels` extended with the pin method, the
  silent-failure list and the RC report corrections.
- Facts → [[wiki/elektrenai/rinkos-atnaujinimas-2026-08]],
  [[wiki/elektrenai/rc-sandoriu-duomenys-2026]]

### Sessions 2026-06-11 → 2026-06-17
Boundaries confirmed, SŽNS overlay, Rimi identified, lt-parcels skill created,
RC mass valuation read, 65 TPDRIS docs + all 16 purpose-change requests OCR'd,
scraping pipeline built (CDP solved DataDome), 119-listing scan, dashboard spec
written, and the 5-session village-name error corrected (block is **Kakliniškių
k.**, not Ausieniškių k.). Full detail: `CONTEXT-ARCHIVE.md`.
