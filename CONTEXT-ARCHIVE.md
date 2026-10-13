# Elektrenai — CONTEXT ARCHIVE

### Session 2026-06-11
- Exact boundaries confirmed (0.00% diff vs RC map)
- SŽNS raster overlay added (LKS94→WGS84 via proj4)
- Rimi logistics centre identified at 0922 (12.85 ha, Darnu Group, ~0.5 km)
- lt-parcels skill created
- Facts → [[wiki/elektrenai/sklypas-4400-1563-8352]]

### Session 2026-06-12
- RC mass valuation: 5 880 € fiscal, real ~6 200 €/ha (zone 8.16)
- Facts → [[wiki/elektrenai/rinkos-skenas-4728-apylinke]]

### Session 2026-06-13
- 65 TPDRIS docs scanned, BPD keitimas K-RJ-42-20-416 active
- Facts → [[wiki/elektrenai/bpd-planavimo-analize]]

### Session 2026-06-14
- Scraping pipeline built (CDP cookie method solved DataDome)
- 134 listings scraped, 45 unique, 15 within 8 km
- All 16 purpose-change requests catalogued via OCR
- Negotiation analysis (figures in the private elektrenai skill, removed from this public repo 2026-10-13)
- Facts → [[wiki/elektrenai/rinkos-skenas-4728-apylinke]], [[wiki/elektrenai/sklypai-master-sarasas]]

### Session 2026-06-15
- All 16 purpose-change docs fully read, 01.3-201/205 not relevant
- dashboard-v1 plan bug fixes

### Session 2026-06-16
- 0005 outcome: decision not yet published (pask_kodas still None in RC ZIP)
- Dashboard reoriented to 3-layer structure (family decision tool)
- Facts → [[wiki/elektrenai/dashboard-v1-koncepcija]]

### Session 2026-06-17 (ankstesnė)
- ZPDRIS archyvas ištirtas (983 unikalūs Elektrėnų sav. projektai) — KPZP ≠ paskirties keitimas
- 16 TPDRIS paskirties keitimo prašymų OCR'inta ir analizuota
- Kritiniai radiniai: 01.3-192 (7910/0001:5 Sabališkių k. → pramonė), 01.3-151 + 01.3-170 (Ausieniškių k. klasteris)
- Facts → [[wiki/elektrenai/paskirties-keitimo-precedentai]]

### Session 2026-06-17 (šis)
- Aruodas pilnas Elektrėnų sav. skenas: 119 unikalių skelbimų (6 puslapiai, CDP metodas)
- Agri 3–8 ha mediana: ~8 600 €/ha (pasiūlymo palyginimas — privačiame skill'e)
- Dashboard 1 turinio spec sukurta: `.planning/dashboard-analysis-content.md`
- Mūsų blokas (0428–0431) = **Kakliniškių k., Elektrėnų sen.** — ne Ausieniškių k. Ausieniškių k. egzistuoja Elektrėnų sen. (~3.5 km, 7910/0007 blokas); atskirai egzistuoja Vievio sen. Ausieniškės (~7 km, pramoninis rajonas prie A1). 5+ sesijų halucinacija taisyta 2026-06-17.
- Wiki atnaujinta: sklypai-master-sarasas.md, sklypas-4400-1563-8352.md, paskirties-keitimo-precedentai.md, dashboard-v1-koncepcija.md

### Session 2026-06-17 (Kakliniškių tyrimas + halucinacijos taisymas)
- Visi 16 paskirties keitimo prašymų OCR'inti su koordinatėmis iš RC ZIP
- **Elektrėnų sen. klasteris patvirtintas (3 prašymai <3.5 km):**
  - 01.3-192: X543608 Y6072904, **350 m** — tas pats blokas 7910/0001, agri→pramonė
  - 01.3-170: X542389 Y6073046, ~1.2 km — agri→gyvenamoji
  - 01.3-151: X546271 Y6070043, ~3.5 km — agri→gyvenamoji (Ausieniškių k. Elektrėnų sen.)
- Pakalniškių k. (01.3-188, 01.3-189) = Vievio sen., ~5–6 km — ne mūsų apylinkė
- Naujų prašymų po 01.3-205 nėra (skentas range 100–350, 2026-06-17)
- Market filtras: 23 skelbimai Kakliniškių k. apylinkės kaimuose; agri ≥1ha mediana 40 909 €/ha
- RC ZIP formavimo_data = ZIP gen. data — aklagatvis paskirties istorija
- **Halucinacijos taisymas (5+ sesijos):** mūsų blokas = Kakliniškių k., ne Ausieniškių k. Pataisyta: sklypai.md, TYRIMO-ISVADOS.md, README.md, CONTEXT.md, sklypai-master-sarasas.md, paskirties-keitimo-precedentai.md, sklypas-4400-1563-8352.md, bpd-planavimo-analize.md, rinkos-skenas-4728-apylinke.md, DECISIONS.md, dashboard-analysis-content.md
- Facts → [[wiki/elektrenai/paskirties-keitimo-precedentai]]

### Session 2026-08-10
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

### Session 2026-10-09
- **Full data refresh** (RC ZIP, register, aruodas, news) — see Status; written up
  in [[wiki/elektrenai/rinkos-atnaujinimas-2026-10]]. Five silent failures found and
  fixed; August map village points were up to ~6 km off.
- **Map**: listings layer rebuilt (126 listings, 22 exact boundaries), 0432 owner +
  zones, water zones (SŽNSĮ art. 99 p. 8 / 100 checked — family block not reduced;
  0428 free area 1.23 → 0.54 ha, 0432 → 0.03 ha), uniform owner labels, build
  version, dark theme default. A full owner name was scrubbed from unpushed history
  before the first push.
- **Private negotiation track opened** — see the skill; official law texts saved
  in `legal/`.
- **Skill** moved from git-ignored `.claude/` to private ai-skills repo with the
  pipeline scripts; a private task added to the skill.

### Session 2026-10-12
- **Private negotiation track** — original documents audited and a counter-proposal
  drafted; all of it in the git-ignored `contracts/` and the skill's
  `references/lease.md` (generator: skill `scripts/build_lease_proposal.py`).
  Nothing about it belongs in this public repo.
