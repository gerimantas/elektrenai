# Elektrenai — CONTEXT

## Project Goal
Research and document land plot Nr. 4400-1563-8352 (cadastral 7910/0001:0431) in Ausieniškių k., Elektrėnų sav. Map parcel boundaries, neighbors, and nearby planning activity. Published as an interactive Google Maps page on GitHub Pages.

## Status

✅ **DONE** — exact boundaries from RC open data, verified against official RC map (0.00% area diff).
Interactive dashboard on GitHub Pages: family strips 0428–0432 + neighbors + Rimi 0922 + precedent
0094 + 0005; SŽNS raster overlay; reconstructed no-build AZ zones with usable-area math; Tyrimas tab
(purpose changes, market prices, access analysis, AZ numbers); owner-name toggle.

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

**REAL transaction values (RC 2026 mass-valuation report, researched 2026-06-12):**
our value zone is **8.16** ("between A1 and railway, intensively urbanizing").
Real RC values: agri ~6 200 €/ha, residential 366 €/a, commercial 596 €/a,
industrial ~350 €/a (modeled, few transactions). Municipality agri trend
5 281→5 562 €/ha (+5.3 %/yr to 2025-07). Listing asks vs real: industrial ×3–4,
residential ×2–2.4, Kakliniškės agri ×16 (speculation premium); the 74.4 a
commercial ask = real value. Family block as agri at real prices ≈ 31 k€.
Full table: vault `wiki/elektrenai/rinkos-skenas-4728-apylinke.md`. Raw docs:
`.firecrawl/rc-aprasomoji_dalis_1191.pdf` (+models/maps), method packaged in
lt-parcels `scripts/rc_valuation_docs.py`. Aruodas (headed Playwright pralaužta
2026-06-12) found 4 extra Ausieniškės listings — see vault note.

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

**Also mapped (2026-06-11):** 0428 (3.05 ha strip NW of 0429, yellow neighbor) and the
industrial precedent **7910/0005:0094** (violet, "rodyti" button in legend) — Gėlių g. 14,
Ausieniškių k., 3.00 ha, pask 995, next to A1 (27 m) near Vievis, listed at 130 k€/ha
(kampas.lt id 1047812). Matched to RC parcel by area + purpose + adjacency to A1 and
Gėlių g. (kampas pin itself lands on a road parcel ~1 km off).

## Rimi Logistics Centre Next Door (found 2026-06-11)

The big building W of the block (visible on satellite) = **7910/0001:0922**, 12.8495 ha,
pask 995, parcel formed 2025-11-26. **Darnu Group is building Rimi's central Baltic
logistics centre**: 31k m2, 60 MEUR, ~800 jobs (Delfi/sa.lt/kronika.lt; press states
12.85 ha — exact match). Adjacent to 0428, i.e. one parcel away from our block.
Strongest industrialization signal for the area. Drawn teal on map with label.

## No-Build Zones in Merged Block (2026-06-11)

Map shows hatched red no-build AZ zones inside the merged block (toggle in legend):

- **Hard ban: 1.2106 ha (24.1%)** of 5.0250 ha — pipeline AZ 1.0973 ha (25 m each side
  of both Minskas–Kaliningradas and GIPL axes, crossing the north part) + road-4728 AZ
  0.1133 ha (20 m beyond road parcel)
- **Heritage AZ 119: 0.8804 ha** (NW part; 0.5351 ha beyond pipeline AZ) — softer:
  construction needs KPD approval, not banned outright. NOTE: RC raster draws 119 as a
  yellow BOUNDARY LINE only (first attempt misread it as 0.02 ha); true extent mapped
  via 15 m identify point grid (±15 m)
- **Fully unrestricted: 3.2793 ha (65.3%)**; up to 3.8144 ha if KPD approves in 119
- Method: RC blocks zone vectors (401) → pipeline/road zones from statutory widths
  (SŽNS law) + OSM axes, verified against RC raster corridor. Scripts:
  `.firecrawl/restricted_v2.py` (zones), `.firecrawl/grid119.py` (heritage grid)
- Tyrimas tab also documents entrance-through-road-AZ legality (SŽNS law art. 19(2):
  allowed with road owner approval; art. 19(3): refusal must be motivated)
- **Neighbor 0428 (3.0501 ha), same method:** hard ban 0.8530 ha (28.0%), heritage AZ
  1.6887 ha (55%), fully free only 1.2265 ha (40.2%), with KPD up to 2.1971 ha.
  Data `.firecrawl/restricted-0428.json`, script `.firecrawl/restricted_0428.py`
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

## Session 2026-06-11 — Map/UI State

- **Visual scheme:** family strips 0428–0431 bright yellow 2px (FAMILY style) with owner
  first names (Virginija/Audra/Viktorija/Aušra ir Gr, "Vardai on/off" button); all other
  parcels neon green (#39FF14); 0005 blue; merged 0429+0430+0431 block — DASHED red
  outline (Polyline + dash icons, polygons can't dash) with 5.0250 ha label.
  Boundary lines sit above AZ layers (parcels z10–11, merged z12, frontage z13; AZ z6–7).
- **Parcels on map:** family 0428–0431, 0432 (fifth twin strip between 0428 and Rimi),
  6 original neighbors, Rimi 0922 (teal→neon), precedent 0094 (pan button), 0005.
- **Labels:** auto-fit via chord spans, anchored at chord midpoints (fitLabelPoint) —
  raw centroids overflow on bent strips like 0431. Hide below 0.35 scale.
- **Legend numbers fixed (was misleading):** single canonical figure — block 5.0250 ha,
  free for building 3.39 ha (excl. road AZ); zone overlap 0.3453 ha stated in Tyrimas
  (5.0250 − 1.2106 hard − 0.5351 heritage-beyond = 3.2793 fully free).
- **Scheduled check:** cloud routine `trig_01Ftvqqm6k7iXRSicMjH53Pv` fires 2026-06-16
  09:00 Vilnius — checks whether 0005 purpose change was approved (publicity ended
  2026-06-15). Results: https://claude.ai/code/routines/trig_01Ftvqqm6k7iXRSicMjH53Pv

## Knowledge Packaged (2026-06-11, end of session)

- **`lt-parcels` skill created** (`C:/Users/retco/.claude/skills/lt-parcels/`, visible to
  Antigravity via .ai-skills junction): parcel lookup (find_parcel.py), neighbors
  (neighbors.py), RC masvert value (masvert.py), SŽNS zones + identify-grid mapping
  (szns_zones.py), plus references with data sources, statutory AZ widths, dead ends
  and Google Maps display patterns. All smoke-tested against this project's data.
  Generic LT-parcel research now works in any project/session.
- Project `CLAUDE.md` added: pointer to CONTEXT.md + 5 operational hard rules.

## Next Session Tasks (optional)

1. Optionally show plot 7910/0008:0037 too
2. Check 0005 purpose-change outcome after 2026-06-16 (cloud routine reports it)
3. Possibly identify heritage object behind AZ 119 (KVR registry) — RC layer gives no name
4. **Continue market scan near road 4728** — vault `wiki/elektrenai/rinkos-skenas-4728-apylinke.md`
   Sesija 2026-06-13 papildė 3 naujais faktais (6, 7 + 1 fakto lentelė):
   - Nauji skelbimai: Gėlių g. 34A (alio ID68730617, 1.03ha sandėliavimo, 65k€), Sabališkių k. 16a agri 14k€
   - Pakalniškių k. 92a agri 5.5k€ = referensinė reali kaina (~RC lygio)
   - remax/ober-haus/capital — nieko apylinkėje (patvirtinta)
   - Sabališkių 16a lokalizacija RC duomenyse nepavyko (nėra kaimo lauko, 49 kandidatai)
   TODO: aruodas retry Sabališkės+Vievis+Kakliniškės (rate-limited); radius search 5km;
   0005 check po 2026-06-16; brokerio skambutis dėl kadastro Nr.

## Sesija 2026-06-14 — Scraping Pipeline + Geocoding

**Sukurti skriptai (`lt-parcels/scripts/`):**
- `radius_villages.py` — RC ZIP → seniunijos per X km nuo sklypo → aruodas slugai
- `market_scan.py` — headed Playwright → struktūruotas JSON (price/area/purpose/url). Turi HTML debug dump kai blocked.
- `geocode_listings.py` — Google Geocoding API (pirmas) + Nominatim fallback + RC paskirtis kodas + atstumas nuo ref. sklypo
- `market_report.py` — grupavimas pagal paskirtį, markdown lentelė

**Pipeline naudojimas (atnaujinta):**
```bash
# 1. Gauti kaimų slugus
python radius_villages.py 7910/0001:0431 --sav 42 --radius 8 --aruodas-slugs

# 2. Scan (headed Chrome su CDP cookie export — žr. žemiau)
python scripts/geocode_listings.py market_raw.json 7910/0001:0431 --sav 42 \
  --out market_geo.json --google-key $GEOCODING_API_KEY \
  --cache .lt-parcels-cache

# 3. Report
python market_report.py market_geo.json --max-km 8 --out market_report.md
```

**aruodas.lt scraping — CDP cookie metodas (2026-06-14 išspręsta):**
- DataDome blokuoja namų/hotspot IP automatiškai (`rt:'c'`)
- Chrome v127+ naudoja App-Bound Encryption — cookies nedekoduojami be admin
- **Sprendimas:** paleisti Chrome su `--remote-debugging-port=9222`, prisijungti rankiniu būdu prie aruodas.lt, tada:
  ```
  # Eksportuoti cookies per CDP
  python .lt-parcels-cache/get_cookies_existing.py  → aruodas_cookies.json
  # Scan su injected cookies
  python .lt-parcels-cache/scan_with_cookies.py
  ```
- Parser'is: kiekvienas listing'as = `sav/k.` → `gatvė` → `kaina €` → `€/a` → `plotas` → `paskirtis` (po `\xa0` normalizacijos)
- Sukurti pagalbiniai skriptai: `get_cookies_cdp.py`, `get_cookies_existing.py`, `scan_with_cookies.py`, `parse_aruodas.py`

**Geocoding — Google API (2026-06-14):**
- Nominatim nežino LT kaimų genityvais (`Kakliniškių k.` → no results)
- Google Geocoding API su `.env` `GEOCODING_API_KEY` (be referrer restriction, atskiras key) → veikia
- 134/134 geocoded via Google; metodas `google` arba `google_village`

**Rinkos scan rezultatai (2026-06-14, 8 km spindulys):**
- **6 seniunijos:** elektrenuose, giluciai, kietaviskese, vievyje, pastrevyje, kazokiskese
- **134 skelbimai** iš viso; **20 per 8 km** nuo 0431
- Raw: `.firecrawl/market_raw.json`, geocoded: `.firecrawl/market_geo.json`, report: `.firecrawl/market_report.md`

**Rinkos suvestinė (8 km, 20 skelbimų):**
| Paskirtis | Kiekis | Mediana €/ha |
|---|---|---|
| Agricultural | 5 | ~11 429 |
| Industrial/Storage | 1 | 197 917 |
| Residential | 10 | 345 070 |
| Garden/Recreation | 2 | 456 237 |

Artimiausias agri: 1.8 km (Žebertonių k., 2.1 ha, 24k€, 11 429 €/ha)

**Kitas žingsnis:** skelbimų markers ant žemėlapio (`sklypas-google.html`) — paspaudus popup su info + link.
5. **tpdris.planuojustatau.lt scanned (2026-06-13):** 65 docs Elektrėnų sav. Key findings:
   S-VT-42-25-302 (7910/0001:889 Žebertoniai, kaimo plėtra, vykstantis);
   K-VT-42-26-8 (A1 koridoriaus komercinė zona Elektrėnų m., baigiamasis etapas 2026-06-12);
   K-RJ-42-20-416 (sav. bendrojo plano keitimas, pradėtas 2026-06-12). 0005 reg. 01.3-192
   TPDRIS nerodo — bus TPDR sistemoje po patvirtinimo (tikrinti po 2026-06-16).

## Sesija 2026-06-14 (II) — Duomenų analizė + Vault dokumentacija

**Duomenų kokybės audit (market_geo.json):**
- 134 įrašai = **45 unikalių** (×3 duplikacija iš aruodas paginacijos)
- Iš 45 — **15 unikalių ≤8 km** (ne 20 kaip report.md rodė)
- **30 įrašų >8 km** — kitos savivaldybės (Vilnius, Trakai, Kaunas, Klaipėda) — scraperio artefaktas
- Ausieniškių koridoriaus 6 pramoniniai skelbimai pipeline **nepateko** — scrapeinti atskirai per playwright

**Sukurti vault dokumentai:**
- `wiki/elektrenai/rinkos-skenas-4728-apylinke.md` — papildyta 8 faktu (sintetinė analizė) + šaltinių nuorodos (web URL + lokalūs failai) prie kiekvieno fakto
- `wiki/elektrenai/sklypai-master-sarasas.md` — **NAUJAS**: kanonininis 21 objekto sąrašas su geolokacija (WGS84+LKS94), šaltiniais, web linkais; pagrindas tolimesniam brainstorm

**Master sąrašo struktūra (21 objektas):**
- 6 Ausieniškių koridoriaus skelbimai (0–1 km, playwright scraped)
- 2 RC objektai (Rimi 0922, paskirties keitimas 0005)
- 1 Sabališkių 16a (elektrenuvaldos.lt)
- 2 Kakliniškių skelbimai (kampas/aruodas)
- 13 radius pipeline unikalūs ≤8 km (market_geo.json, Google geocoded)
- RC realios sandorių kainos (zona 8.16 referensas)

**Geocodavimo problemos:**
- 5.10–5.12 grupė: shared geocode `54.765393, 24.774058` (Kakliniškės village centroid)
- Ausieniškių 1.1–1.6: village-level tik (~54.793, 24.680)
- Sabališkių 16a: koordinatės nežinomos (49 RC kandidatai, tikslus kad. Nr. tik per brokerį)

## Sesija 2026-06-14 (III) — Paskirties keitimo prašymų skenavimas

**Metodas:** `planuojustatau.lt/sites/default/files/01.3-NNN.jpg` — Elektrėnų sav. mero gaunamų
prašymų katalogas. Nuskaityti nr. 100–280, rasta 16 dokumentų. Visi perskaityti OCR.
Skriptas: `.firecrawl/scan_elektrenu_docs.py`, vaizdai: `.firecrawl/elektrenu-docs/`.

**Visi 2026 paskirties keitimo prašymai Elektrėnų sav. (16 dok.):**

| Nr. | Data | Kadastras | Vieta | Keitimas |
|---|---|---|---|---|
| 01.3-106 | 2026-04-13 | 7910/0004:230 | Vidugirių k., Vievio sen. | Agri → **Pramonė/sandėliavimas** |
| 01.3-126 | 2026-04-20 | 4936/0001:427 | Kloninių Mijaugonių k. | Agri → Gyvenamoji |
| 01.3-132 | 2026-04-21 | 7957/0004:35 | Katiliškių k., Pastrėvio sen. | Agri → Gyvenamoji |
| 01.3-141 | 2026-04-24 | 7914/0005:72 | Balceriškių k., Vievio sen. | Agri → Rekreacija |
| 01.3-150 | 2026-04-29 | 7957/0001:0510 | — | Agri → Gyvenamoji |
| 01.3-151 | 2026-04-29 | **7910/0007:619+571** | **Ausieniškių k.** | Agri → **Gyvenamoji** |
| 01.3-152 | 2026-04-29 | 4910/0002:242 | Gilučių k. | Agri → Gyvenamoji |
| 01.3-170 | 2026-05-11 | **7910/0008:37** | **Ausieniškių k.** | Agri → **Gyvenamoji** |
| 01.3-183 | 2026-05-21 | 7914/0001:162 | Lazūnų k. | Pram. → Komercinė |
| 01.3-188 | 2026-05-25 | 7910/0006:667 | Pakalniškių k. | Agri → Gyvenamoji |
| 01.3-189 | 2026-05-25 | 7910/0005:707 | Pakalniškių k. | Agri → Gyvenamoji |
| **01.3-192** | **2026-05-27** | **7910/0001:5** | **Sabališkių k.** | Agri → **Pramonė/sandėliavimas** |
| 01.3-194 | 2026-05-27 | 7914/0001:343 | Lazūnų k. | Agri → Kita |
| 01.3-195 | 2026-05-27 | 7914/0001:342 | Lazūnų k. | Agri → Kita |

**Svarbiausi radiniai:**
- **01.3-151 + 01.3-170**: du gyvenamosios paskirties prašymai **Ausieniškių k.** (7910/0007 blokas) — tas pats kaimas kaip šeimos blokas
- **01.3-192** (mūsų žinomas): pramonė 443 m nuo bloko
- **01.3-106**: pramonė Vidugiriuose (Vievio sen.) — tas pats bangos modelis
- Iš viso 2 pramoniniai + 1 rekreacinis + daugelis gyvenamųjų = aktyvus urbanizacijos frontas

**Derybinė reikšmė:** pirkėjas siūlė 10k€/ha agri kaina — bet apylinkėje 2026 jau 14 paskirties keitimo prašymų vien per 2 mėn. Tai sisteminis, ne pavienio sklypo, reiškinys.

## Sesija 2026-06-14 (IV) — Brainstorm: derybinė analizė

**Kontekstas:** anoniminis pirkėjas siūlo 10k€/ha, skuba, nesiskleidžia.

### Kainų kalibravimas

| Referensas | €/ha | Šaltinis |
|---|---|---|
| RC fiskalinė vertė (mūsų blokas) | 3 510 | masvert.lt 2026-01-01 |
| RC reali sandorių kaina (zona 8.16) | 6 200 | RC masinis vertinimas 2025-07 |
| Bauboniai 3.4 ha agri (6.7 km) | 5 882 | artimiausias RC lygio asking |
| **Pirkėjas siūlo** | **10 000** | — |
| Žebertoniai 2.1 ha agri (1.8 km) | 11 429 | artimiausias agri asking |
| Varžytynių startas (8 km SW) | 14 170 | be spekuliacijos |
| Rekomenduojamas kontrsiūlymas | **16 000–18 000** | Rimi + 0005 + frontažas |
| Jei 0005 patvirtintas | **22 000–25 000** | pirmas pramonės precedentas |

### Pirkėjo profilis (anonimiškumas + skubėjimas)
- Nesiskleidžia → žino daugiau nei rodo
- Skuba → baiminasi kainų kilimo po 0005 rezultato (2026-06-16)
- Profiliai: A) strateginis operatorius (logistika/pramonė), B) tarpininkas-fliperis
- Abiem atvejais derybinė galia pardavėjo pusėje

### Paskirties keitimo klasteris — statistika
- Elektrėnų sav. iš viso: **24 123 sklypų**, **14 973 agri** (RC ZIP 2026)
- 2026 (2 mėn.): **14 paskirties keitimo prašymų** = 0.058% visų / 0.080% agri
- Metinis tempas ~84/m. = **0.56% agri per metus**
- **Ausieniškių k.: 3 iš 14** prašymų (01.3-151, 01.3-170, 01.3-192) — ~1.5% sav. prašymų viename kaime
- Tai klasteris, ne atsitiktinumas — derybinis argumentas

### 0005 dokumento verifikacija
- Dokumentas autentiškas (planuojustatau.lt oficialus katalogas)
- Plotas: **0.3141 ha** (ne "~1+ ha" kaip CONTEXT.md rašė — pataisyta)
- Pareiškėjo vardas neviešas (GDPR) — normalu
- Viešinimas baigėsi 2026-06-15; scheduled check 2026-06-16

### Derybinė strategija
1. **Neatsakyti iki 2026-06-16 vakaro** — palaukti 0005 rezultato
2. Pirkėjui: *"Konsultuojamės su notaru"*
3. **Jei 0005 patvirtintas:** kontrsiūlyti 22k€/ha (~110k€ blokas)
4. **Jei 0005 atidėtas/atmestas:** kontrsiūlyti 16–18k€/ha (~80–90k€)
5. Argumentai: Rimi 0.5 km, 3 paskirties keitimo prašymai Ausieniškių k., 51.9 m kelio frontažas

## Sesija 2026-06-14 (V) — Teritorijų Planavimo Dokumentų Analizė

### TPDRIS aktyvūs dokumentai Elektrėnų sav. (65 viso)

Svarbiausi mūsų blokui (7910/0001):

| TPD Nr. | Tipas | Pavadinimas / Teritorija | Etapas | Data |
|---|---|---|---|---|
| **K-RJ-42-20-416** | Bendrasis plano keitimas | **Elektrėnų sav. BPD keitimas** | Parengiamasis | 2026-06-12 |
| K-VT-42-26-8 | Detalusis planas | Teritorija tarp Šviesos g. ir A1 (komercija/pramogos) | **Baigiamasis** | 2026-06-12 |
| K-VT-42-26-931 | DP korektūra | 7910/0007:288,286,203,233 Abromiškiai | Parengiamasis | 2026-06-02 |
| K-VT-42-24-1165 | DP korektūra | 7910/0007:152,155 Alinkos k. | — | — |
| K-VT-00-25-775 | DP korektūra | **7910/0001:288,289,42** Kakliniškiai | — | — |
| S-VT-42-25-302 | Specialusis | **7910/0001:889** Žebertoniai (kaimo plėtra) | Vykstantis | — |

**Migūčioniai DP (elektrenai.lt):** 7910/0001:74, 46, 79, 19, 77 — tas pats kadastro rajonas kaip šeimos blokas.

### BPD keitimas K-RJ-42-20-416 — aktualumas

- Pradėtas 2026-06-12 (parengiamasis etapas)
- Jau **aktyviai cituojamas** esamuose DP dokumentuose: Sabališkių g. daugiabučių DP tekstas: *"įvertinant rengiamą BPD keitimą (TPD Nr. K-RJ-42-20-416)"* — de facto veikia prieš formalų patvirtinimą
- Šaltinis: elektrenai.lt teritorijų planavimo dokumentų puslapis

### Galiojantis BPD (SS-070-BPL, T00078590) — Radiniai Deryboms

Dokumentas: `Elektrėnų savivaldybės teritorijos bendrasis planas iki 2016 metų`, patvirtintas 2009, ir šiuo metu keitimų rengimo metu tebegalioja kaip bazinis dokumentas.

**Raktiniai radiniai mūsų bloko kontekste:**

#### 1. Elektrėnai–Vievis koridorius = 1A metropolinės ašies dalis
- BPD įvardija Elektrėnai–Vievis kaip **metropolinę ašį** (1A kategorija)
- "Urbanistinė struktūra apims pramonės, verslo įmonių, gamybinių centrų teritorijas"
- Vievio šiaurinė dalis = **pramonė ir logistika prioritetinė zona** (tiesiogiai apima Ausieniškių/Žebertonių apylinkę)

#### 2. Kelias Nr. 4728 = planuojama C2 miesto jungties gatvė
- BPD 4728 (kelias bordering mūsų 0428–0431 bloko vakarinę pusę) **išvardytas** kaip **C2 kategorijos** jungties gatvė tarp Elektrėnų ir Vievio
- C2 = antrojo lygio miesto jungties gatvė → urbanistinis ašis, ne vien kaimo kelias
- **Derybinis argumentas:** bloko frontažas (51.9 m) ant BPD kategorizuotos urbanistinės ašies = komercinio/logistikos sklypo prieiga

#### 3. Ausieniškės = urbanizuojamos teritorijos
- BPD autobusų maršrutas Nr. 3 (209): *"Gilučiai–Mijaugonys–Elektrėnai–Abromiškės–Žebertonys–**Ausieniškės**–Balceriškės–Pylimai–Vievis"*
- Ausieniškės įtrauktos į **oficialų infrastruktūros tinklo planą** — ne kaimas kaip bet koks kitas
- Urbanizuojamos teritorijos plėsis Elektrėnai↔Vievis kryptimi

#### 4. U.7 zonos — verslo/pramonės/logistikos teritorijos
- BPD nustato U.7 zoną = verslo, pramonės, logistikos (potenciali plėtros paskirtis)
- Vievio šiaurinė dalis + Elektrėnų pramonės koridorius patenka į šią zoną
- Mūsų blokas esantis tarp Elektrėnų ir Vievio yra šio koridoriaus dalis

### BPD Radinių Derybinė Reikšmė

| Argumentas | Šaltinis | Svoris |
|---|---|---|
| Kelias 4728 = C2 urbanistinė ašis | BPD SS-070-BPL, susisiekimo sk. | Stiprus — oficialus dok. |
| Ausieniškės autobusų infrastruktūroje | BPD maršrutas Nr. 3 | Vidutinis — infrastruktūros planas |
| Elektrėnai–Vievis = 1A metropolinė ašis | BPD urbanistinė struktūra | Stiprus — strateginis planas |
| K-RJ-42-20-416 jau veikia praktiškai | Sabališkių DP dokumento tekstas | Stiprus — konkreti citata |
| 3 paskirties keitimo prašymai Ausieniškiuose | 01.3-151, 01.3-170, 01.3-192 | Stiprus — statistinis klasteris |

**Pagrindinė žinutė deryboms:** *"Pirkėjas siūlo agri kainą sklypui, kurį oficialus BPD jau 2009 m. įtraukė į metropolinės ašies urbanizacijos zoną, o ant kurio ribos einantis kelias planuotas kaip C2 miesto jungties gatvė."*

### Failai ir web nuorodos

**Lokalūs failai:**
- `.firecrawl/bpd-tekstine-dalis.pdf` — BPD SS-070-BPL tekstinė dalis, 76 psl., 1 MB (parsisiųsta 2026-06-14)
- `.firecrawl/elektrenai-bpd-page.md` — elektrenai.lt BPD puslapis (su visais linkais)
- `.firecrawl/elektrenai-lt-tplan-page.md` — elektrenai.lt TP dokumentų sąrašas (BPD keitimo citata)
- `.firecrawl/planuojustatau/tpdris-elektrenu-results.txt` — 65 TPDRIS dokumentai (Elektrėnų sav.)
- `.firecrawl/planuojustatau/tpdris-26-931-detail.txt` — K-VT-42-26-931 detalės
- `.firecrawl/planuojustatau/tpdris-26-8-detail.txt` — K-VT-42-26-8 detalės
- `.firecrawl/planuojustatau/tpdris-1165-detail.txt` — K-VT-42-24-1165 detalės

**Galiojantis BPD (SS-070-BPL, patvirtintas 2009-04-29, tarybos sprendimas Nr. TS-71):**
- [Tekstinė dalis (elektrenai.lt)](https://elektrenai.lt/get_file.php?file=YTJPYW5wYWxsWjV1eVdaa2F0bHNtOGRpbW1wdWJaWmhhY2ZDcEdPZGFaV1VuY21rWjZuRFlKN0paS0dVeDJyUW5LYVdxWm1jWnFDWXhNYWVsbDVub0dhb3lXVm9wcHFtYmNabm9XWExhTWlZa1plZmJhdG1uMnZQbW1SaWxXS2dtSm5Nb1ptcWxLTnJrNU9pWjVGcDBzeVJ4cDF2b0dTZWFNaVZxR05mbGF1Vm1wcWZsNkxHbG0zWFpXU1h5SmpPbko3SG5HMXBhMmhybDVwclpWNllwR09ZeUp4cWNjSjJiYkNVZW1pdG1MbWVoSmw4bktXVVlKZWxrb1dXZkdtVGxGU1lpV3FHbW9OdXFXaURhYVpxcnAyQWxZQnZlR2Q3YkpHVnBXV1VaWnBqYjVoeFp3JTNEJTNE) ← jau parsisiųsta
- [Žemės naudojimo ir apsaugos reglamentų brėžinys (6.2 MB)](https://elektrenai.lt/get_file.php?file=bVdQSG5tZWx4SjV1eVdSa2FkbHFtNTFpeTJwcWJXWmhhc2VZcEdTZFlwV1luWnVrYnFtVllKJTJGSllxRnN4NWJRbnFhWnFXJTJCY1pxQnN4SmFlWWw2WW9HdW9tV1dicHBTbWJzYVVvWmJMYXNpYmtaaWZiYXRrbjJ2UGxHU1dsV09nbEptZG9XV3FtS09lazJtaWE1Rm4wcDZSbnAyZW9KZWVhTWlUcUdWZmFhdG5tcGlmbDZMSGxwJTJGWFpHUmp5R2ZPbXA2WW5HOXBaR2hvbDVWcVoxNlhubVdrbXAxcWNaTjJiZENYbW1uTm10bk1wSnVjYXFXVXAyekN4Mk5sWG1oaVo2SEhwV2lWbVpOdzFtaWFsTnhuenNxZ3k3QnVxbVJnbHMyVHBaV1hZMjlrYjhnJTNE) ← **žemėlapis — pagrindinė zona mūsų blokui**
- [Susisiekimo sistemos brėžinys (4.8 MB)](https://elektrenai.lt/get_file.php?file=YW1PWW5tcWxscDZmeVdSa1p0bG5tNWhpbUdwdGJaVmhtc2VUcEdtZFpaV1VuWmlrYXFtVVlHN0paNkZqeDVyUW02YVdxWjZjWTZDV3hKR2VhRjZYb0phb21XVm5wcHFtYThhV29XWExaY2lia2NhZmJhdVduNW5QbUdSbGxXZWdaWm1Zb1dhcXg2T2JrNU9pbFpGcDBwdVJtcDF2b0dTZWFjaVdxR05mbDZ0bm1wYWZtcUtUbG03WG1HUmx5R3ZPbUo2Wm5HcHNtR0pxbkpab1pWNWtucGVrbkoxb2NaYUVhdGxscUdQTG10aVptNWVjbTZLV20yZlF3Mk5sWG1kaVkxU2JtRzZvbHZWciUyQjJuNll5QnN6c3VneUxDYnFtWmdhczNHcFdPWGwyOW9iNXclM0Q) ← **kelias 4728 = C2 gatvė čia**
- [Teritorijos vystymo erdvinės struktūros brėžinys (4.8 MB)](https://elektrenai.lt/get_file.php?file=YUdPYm5wYWxtSjV5eVdka2JObHFtOHRpbTJwcmJaWmhhTWVUcEdTZGxKVnFuWm1rbHFtVFlHbkpaS0ZqeDJyUXlhYWJxV3VjWTZDV3hKYWVhRjZZb0dpb21tV2JwcEttYThaa29aakxhOGlZa1oyZm5hdVhuNXJQd21Sb2xXU2dsNW5Lb1cycW1hTnVrMm1pWlpGbjBzdVJtNTF1b0dTZWw4aWFxR0pmWjZ0bG1weWZacUxIbG03WGxXUmx5R3JPeTU3Sm5KbHNsMkptbTVodVpWNWlucFNrbVoxdGNjZUZiOG1XcDJiTGx0bkxvWnVwYXFDWG5KdlNsbU5sWG1saWxGVEhtR3FvdyUyRlZyJTJCMlQ2YVNCdHpwYWduYkJ1cXBoZ2FjMldwV2VYWTI5bGI1ayUzRA)

**BPD keitimas (K-RJ-42-20-416, pradėtas 2020, aktyvus 2026):**
- [TPDRIS viešas peržiūros puslapis](https://tpdris.planuojustatau.lt/tpd.public.view?tpdNr=K-RJ-42-20-416)
- [2025-07-14 patikslinti sprendiniai (rekreacijos aspektas) — elektrenai.lt](https://elektrenai.lt/get_file.php?file=bUdPWW5tZWxrNTV4eVdoa1pNZHIwWmlYbWFKcHEyaWtaY2labzJLUlpKMWxZOGVhbDZXVm5uTEZsNTVwMEdyWW0yR2FuRzJqWXBkbnpwYXBsS0pwbVplaW1KZG5uOFpmY3RCa3FXV1JhOVdjcDhxWm1hTm9tNXJHeEpSZ21KaW9tYUhJb201bGxaWnUwR2VhWk0yYTJaaWttR2FkcEdsaGF0REhsR1dXbFoyWW9NdWJaYW1XWUo3Ymw1dVl5MmZSbnBlYnFtcG1hWmhwekphaGs1VmtabU5rbUdhWmFwWmpiNUpqcFpYR2FjdktiWjJBYXFWa21HWFNrYWRsbldxVmFKZWRuMldrazVweDEyUlZhZEpxMTVpVG1LV1puR24zbWdTWG5tZWRhWlZrcDVsV1o1ZVdvV25OYVpwbmdwclZtcFBMcTU2Z1pwMWwxc2VobHBscW9teW94NnRtcWNKUmNOWm5tcFhOYmRlYmw1cVlhNXFZbTJyTndxU1dvMlJVWmFmTXBtcW9rNVpyMG1xWmFjdG4wNXVieTZ4cXFtUmdiZFBEbVdlV2wyOXFiOHclM0Q)
- [2026-03-17 patikslinti sprendiniai (derinimo pastabos) — elektrenai.lt](https://elektrenai.lt/get_file.php?file=bUdPZW5tV2x3cDV3eVdSa2xjZVcwY3VYbUtKdnE1aWthY2lhbzJTUlpaMW5ZNTZhYXFXWG5tekZaNTVqMEpiWW0yR1huR3lqWkpkcXpwbXBZS0prbVpXaXpKZHFuNWxmYnRDVHFaU1JiZFdjcDh1WmJxT1ltNXZHd3BSaW1KYW9hcUdjb214bG1aWnUwR21hYXMyYTJaYWtsV1pwcEpoaGF0REhsR1dXbFoxcW9KbWJaNm1YWUd6Ylo1dHB5NWpSbkplZHFwbG1aNWhuekppaFpaVm5abVZrbTJ5V2FjVmxjSkpqbVpUUmFzakxxcFp5YUlCbm9HckprcVJnb3BlaFpaV1dtWnFmazUlMkJielpTb2FJSnMxY2lrbXBodHBXZVhtQ2pDMW1LWmFLR1lsY3FwWjFhUm9ackZaNm1XeTJyUW02WEhvMnFnYUtCcTE1T2VsVkNYcDJpa21xaHNtNWFmY3Nob25wZlFhczZkazV5Z2NWZG1vcGJFbEp4bWtaYWdhMVNiVm1lYXc1WnUxbVNlbWRCbHpwJTJCZm1xYWFWMm1pWjhTVXFKU2trNVZzbHN1WGFLbVlYM0xJWjZTWHhXcmRuVzJZY25BJTNE)
- [2024 sprendiniai — Google Drive aplankas](https://drive.google.com/drive/folders/1IjtrjX9xEcA--692YbuvlQdy3Db4Yr1D)
- [2025 sprendiniai — Google Drive aplankas (130 MB JPG)](https://drive.google.com/drive/folders/1ekD4mWL424xekTF6XNFwSnPUXjMxFbBd?usp=sharing) ← **naujausias žemėlapis, reikia žmogaus naršyklėje**

---

## Next Session Tasks

1. **Skelbimų markers žemėlapyje** — `sklypas-google.html`: 21 objektas iš master sąrašo → markers su popup (kaina, €/ha, paskirtis, web link). Naudoti `wiki/elektrenai/sklypai-master-sarasas.md` kaip šaltinį.
2. **0005 paskirties keitimo rezultatas** — scheduled check 2026-06-16 09:00; po to atnaujinti master sąrašą
3. **Aruodas retry** — Sabališkės + Vievis + radius 5km (rate-limited 2026-06-14)
4. **Brainstorm** — remiantis master sąrašu + naujais radiniais: investicinis potencialas, pirkimo/pardavimo scenarijai
5. **Geocode tikslumas** — Ausieniškių 1.1–1.6 tikslios koordinatės (aruodas skelbimų puslapiai)
6. **01.3-201, 01.3-205** — dar 2 neperskaityti dokumentai (atsisiuntė vėliau)
7. **BPD 2025 žemėlapis** — Google Drive (elektrenai.lt): `1_Pagrindinis brėžinys.jpg` 130 MB — parsisiųsti ir patikrinti mūsų bloko zoną vizualiai (reikia žmogaus su naršykle)
