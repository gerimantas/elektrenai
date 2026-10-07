# Elektrenai — CONTEXT

## Status
Data refreshed after 8 weeks (2026-08-10). Market fell 9–45 %; Rimi centre is
BUILT (42 000 m², not 31 000); parcel 0005 still undecided after 2.5 months; the
purpose-change cluster gained zero new members. `sklypas-google.html` rebuilt as
a 3-view app (Žemėlapis / Rinka / Tyrimas) with 53 listings resolved to real RC
boundaries. Committed locally, NOT pushed to Pages.

## Next Tasks
- Deploy the rebuilt map: `git push origin main` + `gh run watch` (6 commits pending)
- Re-derive the counter-offer from August prices — the June range (16–18 k€/ha)
  rested on premises that are both gone; plan: `wiki/elektrenai/rinkos-atnaujinimas-2026-08.md` § 8
- Check 0005 outcome every 2–4 weeks: `python C:/Users/retco/.ai-skills/elektrenai/scripts/check_0005.py`
- Monitor new purpose-change requests via the register page (the `.jpg` probe is
  dead — numbering changed to PZNPB-K####): `scripts/check_requests.py`

## Key Facts
- Plot + neighbors + AZ zones → [[wiki/elektrenai/sklypas-4400-1563-8352]]
- Market scan 8km radius → [[wiki/elektrenai/rinkos-skenas-4728-apylinke]]
- BPD + planning analysis → [[wiki/elektrenai/bpd-planavimo-analize]]
- Master parcel list (21 objects) → [[wiki/elektrenai/sklypai-master-sarasas]]
- Dashboard v1 concept → [[wiki/elektrenai/dashboard-v1-koncepcija]]
- RC/geoportal API research → [[wiki/elektrenai/geoportal-lt-api-research]]
- Paskirties keitimo precedentai (16 prašymų; klasteris NEAUGO per 2026-06→08) → [[wiki/elektrenai/paskirties-keitimo-precedentai]]
- **Rugpjūčio atnaujinimas (naujausi skaičiai)** → [[wiki/elektrenai/rinkos-atnaujinimas-2026-08]]
- **Realūs sandoriai + RC formulės blokui** → [[wiki/elektrenai/rc-sandoriu-duomenys-2026]]
- Projekto darbo eiga, monitoringas, klaidų istorija → `elektrenai` skill
  (`C:/Users/retco/.ai-skills/elektrenai/`)

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

## Files
- `sklypas-google.html` — main interactive map
- `parcels_42/plot_7910_0001_0431.json` — plot GeoJSON
- `.env` / `gen_config.py` / `config.js` — Maps API key (git-ignored)
- `.github/workflows/deploy.yml` — Pages deploy
- `.firecrawl/market_geo_2026-08-10.json` — 124 listings, Google geocoded
- `.firecrawl/listing_by_point.json` — 63 listings resolved to parcels via map pin
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
