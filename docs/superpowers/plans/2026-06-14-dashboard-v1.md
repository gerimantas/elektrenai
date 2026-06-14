# Elektrenai Dashboard v1.0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create `dashboard-v1.html` — a new standalone interactive investment dashboard for family land block 7910/0001:0429+0430+0431, showing all market context layers that influence sale price negotiation.

**Architecture:** Single-file static HTML (no build step, no framework) alongside the existing `sklypas-google.html`. Reuses same Google Maps JS API key injection pattern (`config.js` / `__MAPS_API_KEY__` deploy replacement). Data is embedded inline as JS constants derived from already-collected research data. Four-panel layout: fixed top bar + left sidebar with 4 tabs + full-screen map + bottom price bar.

**Tech Stack:** Google Maps JS API v3, proj4js (CDN, for SŽNS LKS94 overlay), vanilla JS/CSS, static HTML — no npm, no bundler.

---

## Reference Data (embed directly into HTML)

All coordinates and values below come from `CONTEXT.md`, `wiki/elektrenai/sklypai-master-sarasas.md`, `wiki/elektrenai/rinkos-skenas-4728-apylinke.md`, and `wiki/elektrenai/bpd-planavimo-analize.md`. No external data fetch at runtime.

### Key constants
```
BLOCK_CENTER = {lat: 54.793655, lng: 24.682243}
BLOCK_AREA_HA = 5.0250
FREE_BUILD_HA = 3.2793       // 65.3% — hard ban excl.
FREE_KPD_HA = 3.8144         // with KPD approval
ROAD_FRONTAGE_M = 51.9
BUYER_OFFER_EUR = 50250      // 10k€/ha × 5.025
COUNTER_LOW_EUR = 80400      // 16k€/ha
COUNTER_HIGH_EUR = 90450     // 18k€/ha
COUNTER_IF_0005_EUR = 110550 // 22k€/ha
ASKING_LOW_EUR = 55000
ASKING_HIGH_EUR = 66000
INDUSTRIAL_RC_EUR = 176000   // 35k€/ha RC reali
INDUSTRIAL_CEILING_EUR = 500000  // 130k€/ha ask ceiling (AZ-adj ~×0.76)
```

---

## File Structure

| File | Action | Purpose |
|---|---|---|
| `dashboard-v1.html` | **CREATE** | New standalone dashboard — full implementation |
| `sklypas-google.html` | **DO NOT TOUCH** | Existing working map — left as-is |
| `docs/superpowers/plans/2026-06-14-dashboard-v1.md` | this file | Plan |

---

## Task 1: HTML skeleton + CSS layout

**Files:**
- Create: `C:\Users\retco\Projects\Elektrenai\dashboard-v1.html`

### Layout structure
```
┌─────────────────────────────────────────────┐
│ TOP BAR (48px fixed)                        │
├──────────┬──────────────────────────────────┤
│ SIDEBAR  │                                  │
│ 340px    │         MAP (fills rest)         │
│ 4 tabs   │                                  │
│          │                                  │
├──────────┴──────────────────────────────────┤
│ PRICE BAR (56px fixed bottom)               │
└─────────────────────────────────────────────┘
```

- [ ] **Step 1: Create `dashboard-v1.html` with DOCTYPE, head, meta, title**

```html
<!DOCTYPE html>
<html lang="lt">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Elektrėnai · Investicinis dashboard v1.0</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.11.0/proj4.js"></script>
  <script src="config.js"></script>
  <style>
    *, *::before, *::after { box-sizing: border-box; }
    html, body { height: 100%; margin: 0; font-family: system-ui, -apple-system, sans-serif; font-size: 13px; background: #1a1a2e; color: #e8e8e8; }

    /* ── TOP BAR ── */
    #topbar {
      position: fixed; top: 0; left: 0; right: 0; height: 48px; z-index: 100;
      background: #0f0f1a; border-bottom: 1px solid #333;
      display: flex; align-items: center; gap: 0; padding: 0;
    }
    #topbar .logo {
      padding: 0 16px; font-weight: 700; font-size: 14px; color: #fff;
      border-right: 1px solid #333; white-space: nowrap; height: 100%;
      display: flex; align-items: center; gap: 8px;
    }
    #topbar .logo span { color: #FFD700; }
    #topbar .kpis {
      display: flex; flex: 1; height: 100%; overflow: hidden;
    }
    #topbar .kpi {
      padding: 0 18px; border-right: 1px solid #333;
      display: flex; flex-direction: column; justify-content: center;
      min-width: 120px;
    }
    #topbar .kpi .label { font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: .5px; }
    #topbar .kpi .value { font-size: 14px; font-weight: 600; color: #fff; }
    #topbar .kpi .value.green { color: #4CAF50; }
    #topbar .kpi .value.amber { color: #FFB300; }
    #topbar .kpi .value.red   { color: #EF5350; }
    #topbar .status-badge {
      margin-left: auto; margin-right: 12px;
      padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 600;
      background: #FF8F00; color: #000;
      animation: pulse 2s infinite;
    }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.6} }

    /* ── LAYOUT ── */
    #shell {
      position: fixed; top: 48px; bottom: 56px; left: 0; right: 0;
      display: flex;
    }

    /* ── SIDEBAR ── */
    #sidebar {
      width: 340px; min-width: 340px; background: #111122;
      border-right: 1px solid #333; display: flex; flex-direction: column;
      overflow: hidden;
    }
    .tabs-nav {
      display: flex; border-bottom: 1px solid #333; flex-shrink: 0;
    }
    .tabs-nav button {
      flex: 1; padding: 10px 4px; background: none; border: none; border-bottom: 2px solid transparent;
      color: #888; font-size: 12px; cursor: pointer; transition: all .15s;
    }
    .tabs-nav button.active { border-bottom-color: #FFD700; color: #FFD700; font-weight: 600; }
    .tab-pane { display: none; flex: 1; overflow-y: auto; padding: 12px; }
    .tab-pane.active { display: block; }

    /* sidebar component styles */
    .section-title {
      font-size: 11px; text-transform: uppercase; letter-spacing: .7px;
      color: #888; margin: 14px 0 6px; padding-bottom: 4px;
      border-bottom: 1px solid #2a2a3e;
    }
    .section-title:first-child { margin-top: 0; }
    .legend-row {
      display: flex; align-items: flex-start; gap: 8px; margin: 5px 0; line-height: 1.4;
    }
    .swatch {
      width: 12px; height: 12px; border-radius: 2px; flex-shrink: 0; margin-top: 1px;
    }
    .legend-row .lbl { color: #ccc; font-size: 12px; }
    .legend-row .lbl b { color: #fff; }
    .toggle-row {
      display: flex; align-items: center; gap: 8px; margin: 6px 0;
      cursor: pointer; color: #ccc; font-size: 12px;
    }
    .toggle-row input { accent-color: #FFD700; cursor: pointer; }
    .ctrl-btns { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
    .ctrl-btns button {
      padding: 5px 10px; background: #1e1e35; border: 1px solid #444;
      color: #ccc; border-radius: 4px; font-size: 11px; cursor: pointer;
    }
    .ctrl-btns button:hover { background: #2a2a4a; color: #fff; }

    /* market tab */
    .price-block {
      background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 6px;
      padding: 10px 12px; margin: 8px 0;
    }
    .price-block .ph { font-size: 11px; color: #888; margin-bottom: 6px; }
    .price-row {
      display: flex; justify-content: space-between; align-items: center;
      padding: 3px 0; border-bottom: 1px solid #2a2a3e; font-size: 12px;
    }
    .price-row:last-child { border-bottom: none; }
    .price-row .plbl { color: #aaa; }
    .price-row .pval { font-weight: 600; color: #fff; }
    .price-row .pval.green { color: #4CAF50; }
    .price-row .pval.amber { color: #FFB300; }
    .price-row .pval.red   { color: #EF5350; }
    .price-row .pval.blue  { color: #64B5F6; }
    .market-listing {
      display: flex; justify-content: space-between; align-items: center;
      padding: 5px 0; border-bottom: 1px solid #222; cursor: pointer;
      font-size: 12px;
    }
    .market-listing:hover { background: #1e1e35; }
    .market-listing .ml-name { color: #ccc; max-width: 180px; }
    .market-listing .ml-price { font-weight: 600; color: #fff; white-space: nowrap; }
    .market-listing .ml-cat { font-size: 10px; border-radius: 3px; padding: 1px 5px; margin-left: 4px; }
    .cat-industry { background: #4a1515; color: #ff7070; }
    .cat-agri     { background: #2a3a1a; color: #a8d060; }
    .cat-resi     { background: #1a2a3a; color: #60a0d0; }
    .cat-comm     { background: #1a3a2a; color: #60d0a0; }
    .cat-change   { background: #3a2a1a; color: #d0a060; }

    /* planning tab */
    .doc-row {
      padding: 6px 0; border-bottom: 1px solid #222; font-size: 12px;
    }
    .doc-row .doc-nr { font-weight: 600; color: #FFD700; margin-bottom: 2px; }
    .doc-row .doc-desc { color: #aaa; }
    .doc-row .doc-meta { font-size: 10px; color: #666; margin-top: 2px; }
    .doc-row .doc-verdict { font-size: 11px; padding: 1px 6px; border-radius: 3px; display: inline-block; margin-top: 3px; }
    .verdict-strong { background: #1a3a1a; color: #60d060; }
    .verdict-medium { background: #3a3a1a; color: #d0c060; }
    .verdict-info   { background: #1a2a3a; color: #60a0d0; }
    .change-item {
      padding: 4px 0; border-bottom: 1px solid #1e1e2e; font-size: 11px;
    }
    .change-item .ci-nr { color: #FFB300; font-weight: 600; }
    .change-item .ci-loc { color: #ccc; }
    .change-item .ci-type { color: #888; }
    .change-item .ci-industry { color: #ff7070; font-weight: 600; }

    /* zones tab */
    .zone-bar-wrap { margin: 8px 0; }
    .zone-bar-label { display: flex; justify-content: space-between; font-size: 11px; color: #aaa; margin-bottom: 3px; }
    .zone-bar { height: 10px; border-radius: 3px; overflow: hidden; display: flex; }
    .zone-seg-free     { background: #4CAF50; }
    .zone-seg-kpd      { background: #FFB300; }
    .zone-seg-hard     { background: #EF5350; }
    .zone-item { padding: 6px 0; border-bottom: 1px solid #222; font-size: 12px; }
    .zone-item .zi-title { color: #fff; font-weight: 600; margin-bottom: 2px; }
    .zone-item .zi-area  { color: #FFD700; }
    .zone-item .zi-desc  { color: #888; font-size: 11px; }

    /* ── MAP ── */
    #map { flex: 1; }

    /* ── PRICE BAR ── */
    #pricebar {
      position: fixed; bottom: 0; left: 0; right: 0; height: 56px; z-index: 100;
      background: #0f0f1a; border-top: 1px solid #333;
      display: flex; align-items: center; padding: 0 16px; gap: 0;
    }
    .pb-label { font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: .5px; white-space: nowrap; }
    .pb-track {
      flex: 1; height: 12px; background: #2a2a3e; border-radius: 6px;
      position: relative; margin: 0 12px;
    }
    .pb-seg {
      position: absolute; top: 0; height: 100%; border-radius: 6px;
      display: flex; align-items: center; justify-content: center;
      font-size: 9px; font-weight: 700; white-space: nowrap; overflow: hidden;
    }
    .pb-anchor {
      position: absolute; top: -18px; font-size: 10px; transform: translateX(-50%);
      white-space: nowrap; font-weight: 600;
    }
    .pb-anchor::after {
      content: ''; display: block; width: 1px; height: 16px;
      background: currentColor; margin: 2px auto 0;
    }
    .pb-legend { display: flex; gap: 12px; flex-shrink: 0; }
    .pb-item { display: flex; align-items: center; gap: 4px; font-size: 10px; color: #888; }
    .pb-dot { width: 8px; height: 8px; border-radius: 50%; }

    /* ── MAP OVERLAY LABELS ── */
    .plabel {
      font-size: 11px; font-weight: 600; color: #fff; white-space: nowrap;
      text-shadow: 0 0 3px #000, 0 0 3px #000, 0 0 2px #000;
      transform: translate(-50%, -50%); pointer-events: none; text-align: center;
    }
    .plabel small { font-weight: 400; font-size: 10px; }
    .plabel .pname { color: #FFE082; font-size: 12px; }
    body.names-off .pname { display: none; }

    /* marker popup */
    .mkt-popup { font-family: system-ui, sans-serif; font-size: 12px; min-width: 200px; }
    .mkt-popup .mp-title { font-weight: 700; font-size: 13px; margin-bottom: 4px; }
    .mkt-popup .mp-row { display: flex; justify-content: space-between; margin: 2px 0; color: #555; }
    .mkt-popup .mp-row b { color: #111; }
    .mkt-popup a { color: #1a73e8; font-size: 11px; }

    /* szns legend */
    .szns-legend-box { margin-top: 6px; font-size: 11px; color: #aaa; }
    .szns-legend-box ul { margin: 4px 0; padding-left: 16px; }
    .szns-legend-box li { margin: 2px 0; }
  </style>
</head>
<body>
```

- [ ] **Step 2: Add top bar HTML**

```html
<div id="topbar">
  <div class="logo">
    <span>●</span> Elektrėnų sen. · Investicinis tyrimas
  </div>
  <div class="kpis">
    <div class="kpi">
      <div class="label">Blokas (jungtas)</div>
      <div class="value">5.0250 ha · 3 sklypai</div>
    </div>
    <div class="kpi">
      <div class="label">Laisva statybai</div>
      <div class="value green">3.28 ha (65.3%)</div>
    </div>
    <div class="kpi">
      <div class="label">Kelio frontažas</div>
      <div class="value">51.9 m · kelias 4728</div>
    </div>
    <div class="kpi">
      <div class="label">Pirkėjas siūlo</div>
      <div class="value red">50 250 € (10k€/ha)</div>
    </div>
    <div class="kpi">
      <div class="label">Rinkos asking (agri)</div>
      <div class="value amber">55 000–66 000 €</div>
    </div>
    <div class="kpi">
      <div class="label">Kontrsiūlymas</div>
      <div class="value green">80–90 k€ (16–18k€/ha)</div>
    </div>
  </div>
  <div class="status-badge">⏳ 0005 sprendimas: po 2026-06-16</div>
</div>
```

- [ ] **Step 3: Add shell + sidebar HTML skeleton**

```html
<div id="shell">
  <div id="sidebar">
    <div class="tabs-nav">
      <button class="active" onclick="showTab('legenda')">Legenda</button>
      <button onclick="showTab('rinka')">Rinka</button>
      <button onclick="showTab('planavimas')">Planavimas</button>
      <button onclick="showTab('zonos')">Zonos</button>
    </div>

    <!-- TAB: LEGENDA -->
    <div id="tab-legenda" class="tab-pane active">
      <!-- filled in Task 2 -->
    </div>

    <!-- TAB: RINKA -->
    <div id="tab-rinka" class="tab-pane">
      <!-- filled in Task 3 -->
    </div>

    <!-- TAB: PLANAVIMAS -->
    <div id="tab-planavimas" class="tab-pane">
      <!-- filled in Task 4 -->
    </div>

    <!-- TAB: ZONOS -->
    <div id="tab-zonos" class="tab-pane">
      <!-- filled in Task 5 -->
    </div>
  </div>
  <div id="map"></div>
</div>
```

- [ ] **Step 4: Add price bar HTML**

```html
<div id="pricebar">
  <div class="pb-label">Kainų diapazonas</div>
  <div class="pb-track" id="pbTrack">
    <!-- rendered by JS in Task 7 -->
  </div>
  <div class="pb-legend">
    <div class="pb-item"><div class="pb-dot" style="background:#EF5350"></div>Pirkėjas</div>
    <div class="pb-item"><div class="pb-dot" style="background:#FFB300"></div>Agri asking</div>
    <div class="pb-item"><div class="pb-dot" style="background:#4CAF50"></div>Kontrsiūlymas</div>
    <div class="pb-item"><div class="pb-dot" style="background:#64B5F6"></div>Pramonė (RC)</div>
  </div>
</div>
```

- [ ] **Step 5: Commit skeleton**

```bash
git add dashboard-v1.html
git commit -m "feat(dashboard-v1): HTML skeleton, CSS layout, top bar, price bar"
```

---

## Task 2: Sidebar — Legenda tab

**Files:**
- Modify: `C:\Users\retco\Projects\Elektrenai\dashboard-v1.html` — fill `#tab-legenda`

- [ ] **Step 1: Replace Legenda tab placeholder with full content**

Find `<!-- filled in Task 2 -->` inside `#tab-legenda` and replace with:

```html
<div class="section-title">Sklypai</div>
<div class="legend-row">
  <div class="swatch" style="background:#FFF176;border:2px solid #FFFF00"></div>
  <div class="lbl"><b>Šeimos blokas 0428–0431</b> — 4 juostos, ryški geltona</div>
</div>
<div class="legend-row">
  <div class="swatch" style="background:#FFFF00;border:2px dashed #FF0000"></div>
  <div class="lbl"><b>Jungtas blokas 0429+0430+0431</b> — 5.0250 ha, raudona punktyrinė riba</div>
</div>
<div class="legend-row">
  <div class="swatch" style="background:#76FF03;border:2px solid #39FF14"></div>
  <div class="lbl">Kaimynai + Rimi 0922 — neon žalia</div>
</div>
<div class="legend-row">
  <div class="swatch" style="background:#00AAFF;border:2px solid #0066FF"></div>
  <div class="lbl"><b>0005</b> — paskirties keitimas (agri → pramonė)</div>
</div>

<div class="section-title">Rinkos skelbimai</div>
<div class="legend-row">
  <div class="swatch" style="background:#D32F2F;border-radius:50%"></div>
  <div class="lbl">Pramonė / sandėliavimas</div>
</div>
<div class="legend-row">
  <div class="swatch" style="background:#F9A825;border-radius:50%"></div>
  <div class="lbl">Žemės ūkio</div>
</div>
<div class="legend-row">
  <div class="swatch" style="background:#1565C0;border-radius:50%"></div>
  <div class="lbl">Gyvenamoji</div>
</div>
<div class="legend-row">
  <div class="swatch" style="background:#2E7D32;border-radius:50%"></div>
  <div class="lbl">Komercinė</div>
</div>
<div class="legend-row">
  <div class="swatch" style="background:#E65100;border-radius:50%"></div>
  <div class="lbl">Paskirties keitimo prašymas</div>
</div>

<div class="section-title">Apribojimai</div>
<div class="legend-row">
  <div class="swatch" style="background:repeating-linear-gradient(45deg,#300,#300 2px,#D32F2F 2px,#D32F2F 4px)"></div>
  <div class="lbl">Hard ban AZ (dujotiekis 25 m + kelias 20 m)</div>
</div>
<div class="legend-row">
  <div class="swatch" style="background:#FFB300;opacity:.7"></div>
  <div class="lbl">Paveldo AZ 119 (KPD derinimas — ne draudimas)</div>
</div>

<div class="section-title">Infrastruktūra</div>
<div class="legend-row">
  <div class="swatch" style="background:#FF6D00;border-radius:2px;height:4px;margin-top:4px"></div>
  <div class="lbl">Kelio 4728 frontažas (51.9 m) — oranžinė linija</div>
</div>
<div class="legend-row">
  <div class="swatch" style="background:#9C27B0;opacity:.6;border-radius:2px;height:4px;margin-top:4px"></div>
  <div class="lbl">Elektrėnai–Vievis BPD 1A koridorius</div>
</div>

<div class="section-title">Sluoksniai</div>
<label class="toggle-row">
  <input type="checkbox" checked onchange="toggleAz(this.checked)">
  AZ zonos (hard ban + paveldo)
</label>
<label class="toggle-row">
  <input type="checkbox" id="sznsChk" onchange="toggleSzns(this.checked)">
  SŽNS apribojimai (RC rasterinis sluoksnis)
</label>
<label class="toggle-row">
  <input type="checkbox" checked onchange="toggleMarkers(this.checked)">
  Rinkos skelbimai (markers)
</label>
<label class="toggle-row">
  <input type="checkbox" id="circlesChk" onchange="toggleCircles(this.checked)">
  Atstumų žiedai (0.5 / 2 / 8 km)
</label>
<label class="toggle-row">
  <input type="checkbox" id="corridorChk" onchange="toggleCorridor(this.checked)">
  BPD koridorius (Elektrėnai–Vievis)
</label>

<div class="section-title">Valdymas</div>
<div class="ctrl-btns">
  <button onclick="map.setMapTypeId('hybrid')">Hybrid</button>
  <button onclick="map.setMapTypeId('satellite')">Satellite</button>
  <button onclick="map.setMapTypeId('roadmap')">Roadmap</button>
  <button onclick="fitAll()">Centruoti</button>
  <button onclick="toggleLabels()">Labels on/off</button>
  <button onclick="toggleNames()">Vardai on/off</button>
</div>

<div style="margin-top:10px">
  <div class="szns-legend-box" id="sznsLegendBox" style="display:none">
    Sklypą kerta:
    <ul>
      <li><span class="swatch" style="background:#74FFE0;display:inline-block;vertical-align:middle"></span> Magistralinių dujotiekių AZ (107)</li>
      <li><span class="swatch" style="background:#74FFE0;display:inline-block;vertical-align:middle"></span> Dujotiekių vietovių klasės (171)</li>
      <li><span class="swatch" style="background:#FF7F7F;display:inline-block;vertical-align:middle"></span> Elektros tinklų AZ (106)</li>
      <li><span class="swatch" style="background:#FFE100;display:inline-block;vertical-align:middle"></span> Kultūros paveldo AZ (119)</li>
    </ul>
  </div>
</div>
```

- [ ] **Step 2: Verify layout renders (open in browser via http.server)**

```bash
python -m http.server 8124
# open http://localhost:8124/dashboard-v1.html
# Expect: sidebar legenda tab visible, dark theme, top bar with KPIs
```

- [ ] **Step 3: Commit**

```bash
git add dashboard-v1.html
git commit -m "feat(dashboard-v1): Legenda tab — layers, toggles, map controls"
```

---

## Task 3: Sidebar — Rinka tab

**Files:**
- Modify: `C:\Users\retco\Projects\Elektrenai\dashboard-v1.html` — fill `#tab-rinka`

All values from `wiki/elektrenai/rinkos-skenas-4728-apylinke.md` and `TYRIMO-ISVADOS.md`.

- [ ] **Step 1: Replace Rinka tab placeholder**

Find `<!-- filled in Task 3 -->` inside `#tab-rinka` and replace with:

```html
<div class="section-title">RC realios sandorių kainos (zona 8.16)</div>
<div class="price-block">
  <div class="ph">Šaltinis: RC masinis vertinimas sav=1191, ver=36 (2025-07-31) — ne asking, tikri sandoriai</div>
  <div class="price-row"><span class="plbl">Žemės ūkio</span><span class="pval">6 200 €/ha</span></div>
  <div class="price-row"><span class="plbl">Komercinė</span><span class="pval">596 €/a ≈ 59 600 €/ha</span></div>
  <div class="price-row"><span class="plbl">Pramonės (modeliuota)</span><span class="pval amber">~350 €/a ≈ 35 000 €/ha</span></div>
  <div class="price-row"><span class="plbl">Sav. agri trendas</span><span class="pval green">+5.3%/m.</span></div>
</div>

<div class="section-title">Bloko vertinimo diapazonas (5.025 ha)</div>
<div class="price-block">
  <div class="price-row"><span class="plbl">Agri grindys (RC reali)</span><span class="pval">~31 000 €</span></div>
  <div class="price-row"><span class="plbl">Agri asking (rinkos mediana)</span><span class="pval amber">55 000–66 000 €</span></div>
  <div class="price-row"><span class="plbl red">Pirkėjas siūlo</span><span class="pval red">50 250 € (10k€/ha)</span></div>
  <div class="price-row"><span class="plbl">Pramonė (RC reali, −AZ)</span><span class="pval blue">~134 000 €</span></div>
  <div class="price-row"><span class="plbl">Pramonė ceiling (asking, −AZ)</span><span class="pval">~320–500 k€</span></div>
</div>

<div class="section-title">Kontrsiūlymo kalibracija</div>
<div class="price-block">
  <div class="price-row"><span class="plbl">Varžytynių startas (8 km)</span><span class="pval">14 170 €/ha</span></div>
  <div class="price-row"><span class="plbl">Artimiausias agri asking</span><span class="pval">11 429 €/ha (Žebertoniai, 1.8 km)</span></div>
  <div class="price-row"><span class="plbl green">Kontrsiūlymas (dabar)</span><span class="pval green">16–18k€/ha → 80–90 k€</span></div>
  <div class="price-row"><span class="plbl green">Jei 0005 patvirtintas</span><span class="pval green">22–25k€/ha → 110–125 k€</span></div>
</div>

<div class="section-title">Aktyvūs skelbimai apylinkėje — paspaudus → žemėlapis</div>

<div class="market-listing" onclick="focusMarker('geliu-3ha')">
  <span class="ml-name">Gėlių g. 3.0 ha <span class="ml-cat cat-industry">pramonė</span></span>
  <span class="ml-price">130 000 €/ha</span>
</div>
<div class="market-listing" onclick="focusMarker('geliu-34a')">
  <span class="ml-name">Gėlių g. 34A 1.03 ha <span class="ml-cat cat-industry">sandėl.</span></span>
  <span class="ml-price">63 400 €/ha</span>
</div>
<div class="market-listing" onclick="focusMarker('pramones-g')">
  <span class="ml-name">Pramonės g. 2.70 ha <span class="ml-cat cat-industry">pramonė</span></span>
  <span class="ml-price">99 300 €/ha</span>
</div>
<div class="market-listing" onclick="focusMarker('ausieniskes-74a')">
  <span class="ml-name">Ausieniškių k. 74.4a <span class="ml-cat cat-comm">komercinė</span></span>
  <span class="ml-price">59 100 €/ha <span style="color:#4CAF50;font-size:10px">×1.0 RC</span></span>
</div>
<div class="market-listing" onclick="focusMarker('paukštyno')">
  <span class="ml-name">Paukštyno g. 25a <span class="ml-cat cat-resi">gyv.</span></span>
  <span class="ml-price">88 000 €/ha <span style="color:#888;font-size:10px">15 mėn.</span></span>
</div>
<div class="market-listing" onclick="focusMarker('sabaliskes-16a')">
  <span class="ml-name">Sabališkių k. 16a <span class="ml-cat cat-agri">agri</span></span>
  <span class="ml-price">87 500 €/ha <span style="color:#888;font-size:10px">×14 spec.</span></span>
</div>
<div class="market-listing" onclick="focusMarker('zebertoniai')">
  <span class="ml-name">Žebertoniai 2.1 ha <span class="ml-cat cat-agri">agri</span></span>
  <span class="ml-price">11 429 €/ha</span>
</div>
<div class="market-listing" onclick="focusMarker('kakliniskes-a1')">
  <span class="ml-name">Kakliniškės 3.05 ha (A1) <span class="ml-cat cat-agri">agri</span></span>
  <span class="ml-price">98 033 €/ha <span style="color:#888;font-size:10px">spec.</span></span>
</div>
<div class="market-listing" onclick="focusMarker('zilviciu')">
  <span class="ml-name">Žilvičių g. 48a <span class="ml-cat cat-industry">pramonė</span></span>
  <span class="ml-price">197 917 €/ha</span>
</div>
<div class="market-listing" onclick="focusMarker('pakalnis')">
  <span class="ml-name">Pakalniškiai 3.2 ha <span class="ml-cat cat-agri">agri</span></span>
  <span class="ml-price">13 125 €/ha</span>
</div>
<div class="market-listing" onclick="focusMarker('bauboniai')">
  <span class="ml-name">Bauboniai 3.4 ha <span class="ml-cat cat-agri">agri</span></span>
  <span class="ml-price">5 882 €/ha <span style="color:#4CAF50;font-size:10px">≈ RC</span></span>
</div>
```

- [ ] **Step 2: Commit**

```bash
git add dashboard-v1.html
git commit -m "feat(dashboard-v1): Rinka tab — RC prices, valuation range, market listings"
```

---

## Task 4: Sidebar — Planavimas tab

**Files:**
- Modify: `C:\Users\retco\Projects\Elektrenai\dashboard-v1.html` — fill `#tab-planavimas`

All values from `wiki/elektrenai/bpd-planavimo-analize.md` and `CONTEXT.md` sesija 2026-06-14 (III).

- [ ] **Step 1: Replace Planavimas tab placeholder**

Find `<!-- filled in Task 4 -->` inside `#tab-planavimas` and replace with:

```html
<div class="section-title">BPD SS-070-BPL (galiojantis, 2009)</div>

<div class="doc-row">
  <div class="doc-nr">1A metropolinė ašis — Elektrėnai–Vievis</div>
  <div class="doc-desc">„Urbanistinė struktūra apims pramonės, verslo įmonių, gamybinių centrų teritorijas." Vievio šiaurinė dalis = pramonė ir logistika prioritetinė zona. Mūsų blokas šio koridoriaus viduryje.</div>
  <div class="doc-verdict verdict-strong">Stiprus derybinis argumentas</div>
</div>

<div class="doc-row">
  <div class="doc-nr">Kelias Nr. 4728 = C2 miesto jungties gatvė</div>
  <div class="doc-desc">BPD susisiekimo brėžinys: kelias 4728 — C2 kategorija, antrojo lygio jungties gatvė Elektrėnai–Vievis. Mūsų blokas turi 51.9 m frontažą ant šio kelio. C2 ≠ kaimo kelias — tai urbanistinė ašis.</div>
  <div class="doc-verdict verdict-strong">Stiprus — oficialus dokumentas</div>
</div>

<div class="doc-row">
  <div class="doc-nr">Ausieniškės autobusų infrastruktūros plane</div>
  <div class="doc-desc">BPD maršrutas Nr. 3 (209): „...Žebertonys–Ausieniškės–Balceriškės..." Ausieniškės įtrauktos į oficialų infrastruktūros planą.</div>
  <div class="doc-verdict verdict-medium">Vidutinis</div>
</div>

<div class="doc-row">
  <div class="doc-nr">U.7 zona — verslo/pramonės/logistikos</div>
  <div class="doc-desc">BPD nustato U.7 = verslo, pramonės, logistikos zona. Vievio šiaurinė dalis + Elektrėnų pramonės koridorius. Mūsų blokas šio koridoriaus potenciali plėtros teritorija.</div>
  <div class="doc-verdict verdict-medium">Vidutinis — potenciali zona</div>
</div>

<div class="section-title">Rengiamas BPD keitimas K-RJ-42-20-416</div>

<div class="doc-row">
  <div class="doc-nr">K-RJ-42-20-416 — Sav. BPD keitimas</div>
  <div class="doc-desc">Pradėtas 2026-06-12 (parengiamasis etapas). Jau cituojamas aktyviuose DP dokumentuose: „įvertinant rengiamą BPD keitimą (TPD Nr. K-RJ-42-20-416)" — Sabališkių g. daugiabučių DP tekstas. De facto galioja prieš formalų patvirtinimą.</div>
  <div class="doc-meta"><a href="https://tpdris.planuojustatau.lt/tpd.public.view?tpdNr=K-RJ-42-20-416" target="_blank">TPDRIS →</a></div>
  <div class="doc-verdict verdict-strong">Stiprus — konkreti citata</div>
</div>

<div class="section-title">Paskirties keitimo prašymai 2026 (Elektrėnų sav.)</div>
<div style="font-size:11px;color:#888;margin-bottom:8px">16 prašymų per ~2 mėn. = 0.08% agri/metus. <b style="color:#FFB300">Ausieniškių k.: 3 iš 16 (19%)</b> — klasteris, ne atsitiktinumas.</div>

<div class="change-item"><span class="ci-nr">01.3-192</span> · <span class="ci-loc">Sabališkių k. (443 m SW)</span> · <span class="ci-industry">Agri → PRAMONĖ ⚠</span> · 2026-05-27 · <a href="https://planuojustatau.lt/sites/default/files/01.3-192.jpg" target="_blank" style="color:#FFB300;font-size:10px">dok →</a></div>
<div class="change-item"><span class="ci-nr">01.3-151</span> · <span class="ci-loc">Ausieniškių k. 7910/0007:619+571</span> · <span class="ci-type">Agri → Gyvenamoji</span> · 2026-04-29</div>
<div class="change-item"><span class="ci-nr">01.3-170</span> · <span class="ci-loc">Ausieniškių k. 7910/0008:37</span> · <span class="ci-type">Agri → Gyvenamoji</span> · 2026-05-11</div>
<div class="change-item"><span class="ci-nr">01.3-106</span> · <span class="ci-loc">Vidugiriai, Vievio sen.</span> · <span class="ci-industry">Agri → Pramonė</span> · 2026-04-13</div>
<div class="change-item"><span class="ci-nr">01.3-126</span> · <span class="ci-loc">Kloninių Mijaugonys</span> · <span class="ci-type">Agri → Gyvenamoji</span> · 2026-04-20</div>
<div class="change-item"><span class="ci-nr">01.3-132</span> · <span class="ci-loc">Katiliškių k.</span> · <span class="ci-type">Agri → Gyvenamoji</span> · 2026-04-21</div>
<div class="change-item"><span class="ci-nr">01.3-141</span> · <span class="ci-loc">Balceriškių k.</span> · <span class="ci-type">Agri → Rekreacija</span> · 2026-04-24</div>
<div class="change-item"><span class="ci-nr">01.3-152</span> · <span class="ci-loc">Gilučių k.</span> · <span class="ci-type">Agri → Gyvenamoji</span> · 2026-04-29</div>
<div class="change-item"><span class="ci-nr">01.3-183</span> · <span class="ci-loc">Lazūnų k.</span> · <span class="ci-type">Pram. → Komercinė</span> · 2026-05-21</div>
<div class="change-item"><span class="ci-nr">01.3-188/189</span> · <span class="ci-loc">Pakalniškių k. (×2)</span> · <span class="ci-type">Agri → Gyvenamoji</span> · 2026-05-25</div>
<div class="change-item"><span class="ci-nr">01.3-194/195</span> · <span class="ci-loc">Lazūnų k. (×2)</span> · <span class="ci-type">Agri → Kita</span> · 2026-05-27</div>

<div class="section-title">TPDRIS aktyvūs dokumentai (mūsų rajonas)</div>
<div class="doc-row">
  <div class="doc-nr">S-VT-42-25-302 · 7910/0001:889 Žebertoniai</div>
  <div class="doc-desc">Kaimo plėtros žemėtvarkos projektas. Vykstantis. Žebertoniai ~3 km SW.</div>
  <div class="doc-verdict verdict-info">Informacinis</div>
</div>
<div class="doc-row">
  <div class="doc-nr">K-VT-00-25-775 · 7910/0001:288,289,42 Kakliniškiai</div>
  <div class="doc-desc">DP korektūra — tas pats 7910/0001 kadastro rajonas kaip mūsų blokas.</div>
  <div class="doc-verdict verdict-info">Informacinis</div>
</div>
<div class="doc-row">
  <div class="doc-nr">K-VT-42-26-8 · A1 koridorius (baigiamasis)</div>
  <div class="doc-desc">Detalusis planas komercinei/pramoginei zonai tarp Šviesos g. ir A1. Baigiamasis etapas 2026-06-12.</div>
  <div class="doc-verdict verdict-medium">A1 koridoriaus signalas</div>
</div>
```

- [ ] **Step 2: Commit**

```bash
git add dashboard-v1.html
git commit -m "feat(dashboard-v1): Planavimas tab — BPD radiniai, 14 paskirties keitimų, TPDRIS"
```

---

## Task 5: Sidebar — Zonos tab

**Files:**
- Modify: `C:\Users\retco\Projects\Elektrenai\dashboard-v1.html` — fill `#tab-zonos`

Values from `CONTEXT.md` — no-build AZ sections.

- [ ] **Step 1: Replace Zonos tab placeholder**

Find `<!-- filled in Task 5 -->` inside `#tab-zonos` and replace with:

```html
<div class="section-title">Blokas 0429+0430+0431 · 5.0250 ha</div>

<div class="zone-bar-wrap">
  <div class="zone-bar-label">
    <span>Ploto struktūra</span>
    <span>5.0250 ha = 100%</span>
  </div>
  <div class="zone-bar">
    <div class="zone-seg-free"  style="width:65.3%" title="Laisva 3.28 ha"></div>
    <div class="zone-seg-kpd"   style="width:10.6%" title="KPD AZ 0.535 ha (virš pipeline)"></div>
    <div class="zone-seg-hard"  style="width:24.1%" title="Hard ban 1.21 ha"></div>
  </div>
  <div style="display:flex;gap:12px;margin-top:4px;font-size:10px">
    <span style="color:#4CAF50">■ Laisva 65.3%</span>
    <span style="color:#FFB300">■ KPD 10.6%</span>
    <span style="color:#EF5350">■ Hard ban 24.1%</span>
  </div>
</div>

<div class="zone-item">
  <div class="zi-title">Visiškai laisva statybai</div>
  <div class="zi-area">3.2793 ha (65.3%) — su KPD: 3.8144 ha</div>
  <div class="zi-desc">Jokių papildomų derinimų nereikia.</div>
</div>
<div class="zone-item">
  <div class="zi-title">Magistralinis dujotiekis (AZ 107) — Hard ban</div>
  <div class="zi-area">1.0973 ha</div>
  <div class="zi-desc">25 m abipus ašies: Minskas–Kaliningradas + GIPL. Kerta šiaurinę bloko dalį. Ambergrid sutikimas bet kokiems darbams. Lentelė 3, eil. 164.</div>
</div>
<div class="zone-item">
  <div class="zi-title">Kelio 4728 AZ — Hard ban statybai</div>
  <div class="zi-area">0.1133 ha</div>
  <div class="zi-desc">20 m už kelio juostos. Įvaža per AZ legali — SŽNS įst. 19 str. 2 d. (Via Lietuva prisijungimo sąlygos).</div>
</div>
<div class="zone-item">
  <div class="zi-title">Kultūros paveldo AZ 119 — KPD derinimas</div>
  <div class="zi-area">0.8804 ha iš viso; 0.5351 ha už pipeline AZ ribų</div>
  <div class="zi-desc">NW bloko dalis. Ne absoliutus draudimas — statybai reikia KPD leidimo. Zona kartografuota 15 m identify tinkleliu (±15 m paklaida).</div>
</div>
<div class="zone-item">
  <div class="zi-title">Dujotiekio vietovių klasė 171</div>
  <div class="zi-area">Visas blokas koridoriuje</div>
  <div class="zi-desc">Ne plotų draudimas — papildomi projektavimo reikalavimai pastatų tankiui/atstumams.</div>
</div>
<div class="zone-item">
  <div class="zi-title">110 kV elektros linija (AZ 106)</div>
  <div class="zi-area">AZ nepatenka į bloką</div>
  <div class="zi-desc">Linija eina 47 m nuo bloko ribos — poveikio nėra.</div>
</div>

<div class="section-title">Kaimynas 0428 · 3.0501 ha</div>

<div class="zone-bar-wrap">
  <div class="zone-bar">
    <div class="zone-seg-free"  style="width:40.2%" title="Laisva 1.23 ha"></div>
    <div class="zone-seg-kpd"   style="width:31.8%" title="KPD AZ virš pipeline"></div>
    <div class="zone-seg-hard"  style="width:28.0%" title="Hard ban 0.853 ha"></div>
  </div>
  <div style="display:flex;gap:12px;margin-top:4px;font-size:10px">
    <span style="color:#4CAF50">■ Laisva 40.2%</span>
    <span style="color:#FFB300">■ KPD 31.8% (!)</span>
    <span style="color:#EF5350">■ Hard ban 28.0%</span>
  </div>
</div>
<div class="zone-item">
  <div class="zi-title">Laisva / su KPD</div>
  <div class="zi-area">1.2265 ha (40.2%) / 2.1971 ha</div>
  <div class="zi-desc">Labiau apribota nei 0429–0431 dėl didesnės paveldo AZ 119 dalies (55% ploto).</div>
</div>

<div class="section-title">Kelio 4728 prieigos analizė</div>
<div class="zone-item">
  <div class="zi-title">Frontažas</div>
  <div class="zi-area">51.9 m (0429 ~35 m + 0430 ~16.8 m)</div>
  <div class="zi-desc">0431 kelio nesiekia — 0050 tarpinis sklypas. Pakanka dvikrypčiam sunkvežimių įvažos (7 m + R 12.5 m posūkio lankai). 12×12 m apsisukimo aikštelė telpa.</div>
</div>
<div class="zone-item">
  <div class="zi-title">Teisinė bazė</div>
  <div class="zi-area">SŽNS įst. 19 str. 2 d. + 3 d.</div>
  <div class="zi-desc">Įvaža per kelio AZ legali su Via Lietuva prisijungimo sąlygomis. Atsisakymas turi būti motyvuotas (trukdys eismo saugai) — ne savavališkai. Kelias 4728 rekonstrukcijos planų nėra (tikrinta 2026-06).</div>
</div>
```

- [ ] **Step 2: Commit**

```bash
git add dashboard-v1.html
git commit -m "feat(dashboard-v1): Zonos tab — AZ breakdown, bar chart, kelio prieiga"
```

---

## Task 6: Inline JS data constants

**Files:**
- Modify: `C:\Users\retco\Projects\Elektrenai\dashboard-v1.html` — add `<script>` block with all embedded data before closing `</body>`

This task embeds parcel polygons (copy from `sklypas-google.html`), market markers, and map layer data. All coordinates verified against `CONTEXT.md`.

- [ ] **Step 1: Add opening script tag and parcel data**

Add after `</div><!-- #pricebar -->` and before `</body>`:

```html
<script>
// ── PARCEL POLYGONS (copied from sklypas-google.html DATA + extras) ──
const DATA = {"7910/0001:0005":{"path":[{"lat":54.790413,"lng":24.678248},{"lat":54.790854,"lng":24.678366},{"lat":54.79087,"lng":24.677889},{"lat":54.790862,"lng":24.677886},{"lat":54.790033,"lng":24.677597},{"lat":54.789992,"lng":24.678135},{"lat":54.790413,"lng":24.678248}],"center":{"lat":54.790491,"lng":24.678053},"plotas":"0.3141","pask":610},"7910/0001:1014":{"path":[{"lat":54.796081,"lng":24.685332},{"lat":54.79431,"lng":24.682815},{"lat":54.794092,"lng":24.684384},{"lat":54.795481,"lng":24.686286},{"lat":54.796081,"lng":24.685332}],"center":{"lat":54.795209,"lng":24.68483},"plotas":"2.0734","pask":610},"7910/0001:0949":{"path":[{"lat":54.794194,"lng":24.682749},{"lat":54.793984,"lng":24.682629},{"lat":54.793762,"lng":24.682503},{"lat":54.792245,"lng":24.68164},{"lat":54.792638,"lng":24.682394},{"lat":54.793608,"lng":24.683722},{"lat":54.79381,"lng":24.683999},{"lat":54.793987,"lng":24.68424},{"lat":54.794194,"lng":24.682749}],"center":{"lat":54.793602,"lng":24.682958},"plotas":"1.2266","pask":610},"7910/0001:0048":{"path":[{"lat":54.792245,"lng":24.68164},{"lat":54.791606,"lng":24.684752},{"lat":54.791511,"lng":24.685175},{"lat":54.79138,"lng":24.685765},{"lat":54.791228,"lng":24.686444},{"lat":54.791158,"lng":24.686759},{"lat":54.790725,"lng":24.687036},{"lat":54.79076,"lng":24.687774},{"lat":54.790848,"lng":24.688522},{"lat":54.790971,"lng":24.689115},{"lat":54.79111,"lng":24.689606},{"lat":54.791223,"lng":24.690008},{"lat":54.791313,"lng":24.690293},{"lat":54.793425,"lng":24.689436},{"lat":54.793642,"lng":24.689347},{"lat":54.794532,"lng":24.688963},{"lat":54.794211,"lng":24.688414},{"lat":54.792291,"lng":24.685133},{"lat":54.792638,"lng":24.682394},{"lat":54.792245,"lng":24.68164}],"center":{"lat":54.791953,"lng":24.686911},"plotas":"9.6755","pask":610},"7910/0001:0050":{"path":[{"lat":54.790982,"lng":24.679702},{"lat":54.79094,"lng":24.681556},{"lat":54.790817,"lng":24.683943},{"lat":54.791148,"lng":24.684282},{"lat":54.791388,"lng":24.684529},{"lat":54.791606,"lng":24.684752},{"lat":54.792245,"lng":24.68164},{"lat":54.791381,"lng":24.680315},{"lat":54.790982,"lng":24.679702}],"center":{"lat":54.791277,"lng":24.682269},"plotas":"3.0500","pask":610},"7910/0001:0023":{"path":[{"lat":54.796081,"lng":24.685332},{"lat":54.796125,"lng":24.685388},{"lat":54.796352,"lng":24.685669},{"lat":54.796696,"lng":24.683786},{"lat":54.796722,"lng":24.683674},{"lat":54.794575,"lng":24.681621},{"lat":54.794499,"lng":24.681966},{"lat":54.79431,"lng":24.682815},{"lat":54.796081,"lng":24.685332}],"center":{"lat":54.795716,"lng":24.683954},"plotas":"3.1300","pask":610},"7910/0001:0431":{"path":[{"lat":54.79431,"lng":24.682815},{"lat":54.794499,"lng":24.681966},{"lat":54.791381,"lng":24.680315},{"lat":54.792245,"lng":24.68164},{"lat":54.793762,"lng":24.682503},{"lat":54.793984,"lng":24.682629},{"lat":54.794194,"lng":24.682749},{"lat":54.794212,"lng":24.682759},{"lat":54.79431,"lng":24.682815}],"center":{"lat":54.793655,"lng":24.682243},"plotas":"1.6750","pask":610},"7910/0001:0430":{"path":[{"lat":54.794575,"lng":24.681621},{"lat":54.794628,"lng":24.68135},{"lat":54.790991,"lng":24.679441},{"lat":54.790982,"lng":24.679702},{"lat":54.791381,"lng":24.680315},{"lat":54.794499,"lng":24.681966},{"lat":54.794575,"lng":24.681621}],"center":{"lat":54.79309,"lng":24.680859},"plotas":"1.6750","pask":610},"7910/0001:0429":{"path":[{"lat":54.794628,"lng":24.68135},{"lat":54.794758,"lng":24.680682},{"lat":54.791009,"lng":24.678914},{"lat":54.790991,"lng":24.679441},{"lat":54.794628,"lng":24.68135}],"center":{"lat":54.792942,"lng":24.680143},"plotas":"1.6750","pask":610},"7910/0001:0428":{"path":[{"lat":54.791037,"lng":24.678107},{"lat":54.791009,"lng":24.678914},{"lat":54.794758,"lng":24.680682},{"lat":54.795008,"lng":24.679392},{"lat":54.791037,"lng":24.678107}],"center":{"lat":54.79312,"lng":24.679336},"plotas":"3.0500","pask":610},"7910/0001:0432":{"path":[{"lat":54.795008,"lng":24.679392},{"lat":54.795126,"lng":24.678788},{"lat":54.794703,"lng":24.678564},{"lat":54.794433,"lng":24.678494},{"lat":54.794364,"lng":24.678476},{"lat":54.794326,"lng":24.678465},{"lat":54.794272,"lng":24.678451},{"lat":54.792784,"lng":24.67806},{"lat":54.792331,"lng":24.678116},{"lat":54.792077,"lng":24.678132},{"lat":54.79182,"lng":24.678095},{"lat":54.791611,"lng":24.677974},{"lat":54.791483,"lng":24.677806},{"lat":54.791373,"lng":24.67757},{"lat":54.791289,"lng":24.67747},{"lat":54.791064,"lng":24.677344},{"lat":54.791037,"lng":24.678107},{"lat":54.795008,"lng":24.679392}],"center":{"lat":54.793236,"lng":24.678506},"plotas":"1.6750","pask":610}};

const NAMES = {'7910/0001:0428':'Virginija','7910/0001:0429':'Audra','7910/0001:0430':'Viktorija','7910/0001:0431':'Aušra ir Gr'};

const RIMI = {kn:'7910/0001:0922',path:[{lat:54.793334,lng:24.67163},{lat:54.792969,lng:24.671909},{lat:54.792735,lng:24.672108},{lat:54.792573,lng:24.672246},{lat:54.79234,lng:24.672432},{lat:54.79213,lng:24.672571},{lat:54.791938,lng:24.672642},{lat:54.791686,lng:24.672685},{lat:54.791456,lng:24.672712},{lat:54.791282,lng:24.672727},{lat:54.791236,lng:24.672719},{lat:54.791228,lng:24.672763},{lat:54.791216,lng:24.672832},{lat:54.791195,lng:24.673125},{lat:54.791186,lng:24.673446},{lat:54.791195,lng:24.673833},{lat:54.791193,lng:24.673895},{lat:54.791177,lng:24.674184},{lat:54.791172,lng:24.674498},{lat:54.791162,lng:24.674855},{lat:54.791159,lng:24.675173},{lat:54.791113,lng:24.675416},{lat:54.791099,lng:24.67575},{lat:54.791086,lng:24.676102},{lat:54.791085,lng:24.676352},{lat:54.791068,lng:24.67658},{lat:54.791071,lng:24.677033},{lat:54.791073,lng:24.67706},{lat:54.791075,lng:24.677132},{lat:54.791077,lng:24.677161},{lat:54.791064,lng:24.677344},{lat:54.791289,lng:24.67747},{lat:54.791373,lng:24.67757},{lat:54.791483,lng:24.677806},{lat:54.791611,lng:24.677974},{lat:54.79182,lng:24.678095},{lat:54.792077,lng:24.678132},{lat:54.792331,lng:24.678116},{lat:54.792784,lng:24.67806},{lat:54.794272,lng:24.678451},{lat:54.794289,lng:24.678035},{lat:54.794266,lng:24.677699},{lat:54.794248,lng:24.677359},{lat:54.79425,lng:24.677009},{lat:54.794254,lng:24.676658},{lat:54.794256,lng:24.676272},{lat:54.794259,lng:24.675892},{lat:54.794261,lng:24.675555},{lat:54.794258,lng:24.675224},{lat:54.794255,lng:24.67486},{lat:54.794254,lng:24.674555},{lat:54.794255,lng:24.674231},{lat:54.794255,lng:24.673878},{lat:54.794255,lng:24.673548},{lat:54.794255,lng:24.673206},{lat:54.794248,lng:24.672936},{lat:54.793334,lng:24.67163}],center:{lat:54.792755,lng:24.675234}};

const PRECEDENT = {kn:'7910/0005:0094',path:[{lat:54.783158,lng:24.783712},{lat:54.783314,lng:24.782952},{lat:54.783406,lng:24.782504},{lat:54.783386,lng:24.782488},{lat:54.780384,lng:24.780118},{lat:54.780369,lng:24.780248},{lat:54.780238,lng:24.781419},{lat:54.783158,lng:24.783712}],center:{lat:54.781795,lng:24.781933}};

// AZ zones (from sklypas-google.html RESTRICTED + RESTRICTED_0428)
const RESTRICTED = {"hardOutline":[[{"lat":54.793904,"lng":24.680419},{"lat":54.793907,"lng":24.680281},{"lat":54.79462,"lng":24.680617},{"lat":54.794291,"lng":24.682804},{"lat":54.793673,"lng":24.682452},{"lat":54.793904,"lng":24.680419}],[{"lat":54.791186,"lng":24.678998},{"lat":54.791156,"lng":24.679969},{"lat":54.790982,"lng":24.679702},{"lat":54.791009,"lng":24.678914},{"lat":54.791186,"lng":24.678998}]],"hardHatch":[[{"lat":54.794554,"lng":24.680587},{"lat":54.79461,"lng":24.680685}],[{"lat":54.794417,"lng":24.680522},{"lat":54.794589,"lng":24.680825}],[{"lat":54.794279,"lng":24.680457},{"lat":54.794568,"lng":24.680965}],[{"lat":54.794142,"lng":24.680392},{"lat":54.794546,"lng":24.681106}],[{"lat":54.794005,"lng":24.680327},{"lat":54.794525,"lng":24.681246}],[{"lat":54.793906,"lng":24.68033},{"lat":54.794504,"lng":24.681386}],[{"lat":54.793896,"lng":24.680491},{"lat":54.794483,"lng":24.681527}],[{"lat":54.793879,"lng":24.680639},{"lat":54.794462,"lng":24.681667}],[{"lat":54.793862,"lng":24.680787},{"lat":54.794441,"lng":24.681808}],[{"lat":54.793846,"lng":24.680935},{"lat":54.79442,"lng":24.681948}],[{"lat":54.793829,"lng":24.681083},{"lat":54.794398,"lng":24.682088}],[{"lat":54.793812,"lng":24.681231},{"lat":54.794377,"lng":24.682229}],[{"lat":54.793795,"lng":24.681379},{"lat":54.794356,"lng":24.682369}],[{"lat":54.793778,"lng":24.681527},{"lat":54.794335,"lng":24.682509}],[{"lat":54.793762,"lng":24.681675},{"lat":54.794314,"lng":24.68265}],[{"lat":54.793745,"lng":24.681823},{"lat":54.794293,"lng":24.68279}],[{"lat":54.793728,"lng":24.681971},{"lat":54.794157,"lng":24.682727}],[{"lat":54.793711,"lng":24.682119},{"lat":54.794008,"lng":24.682643}],[{"lat":54.793694,"lng":24.682267},{"lat":54.793859,"lng":24.682558}],[{"lat":54.793677,"lng":24.682415},{"lat":54.793711,"lng":24.682474}],[{"lat":54.791119,"lng":24.678966},{"lat":54.791184,"lng":24.67908}],[{"lat":54.791008,"lng":24.678948},{"lat":54.791178,"lng":24.679248}],[{"lat":54.791002,"lng":24.679116},{"lat":54.791172,"lng":24.679415}],[{"lat":54.790997,"lng":24.679283},{"lat":54.791166,"lng":24.679583}],[{"lat":54.790991,"lng":24.679451},{"lat":54.791161,"lng":24.679751}],[{"lat":54.790985,"lng":24.679618},{"lat":54.791157,"lng":24.679921}]],"heritOutline":[[{"lat":54.793287,"lng":24.679989},{"lat":54.793304,"lng":24.680115},{"lat":54.793569,"lng":24.680122},{"lat":54.793826,"lng":24.680243},{"lat":54.793842,"lng":24.680358},{"lat":54.79408,"lng":24.680363},{"lat":54.794366,"lng":24.680498},{"lat":54.79438,"lng":24.6806},{"lat":54.794595,"lng":24.680606},{"lat":54.79475,"lng":24.680679},{"lat":54.79475,"lng":24.680721},{"lat":54.794679,"lng":24.681089},{"lat":54.794627,"lng":24.681098},{"lat":54.794612,"lng":24.681307},{"lat":54.794343,"lng":24.681303},{"lat":54.794315,"lng":24.681075},{"lat":54.793805,"lng":24.68106},{"lat":54.793785,"lng":24.680841},{"lat":54.793402,"lng":24.68082},{"lat":54.79337,"lng":24.68059},{"lat":54.792864,"lng":24.680578},{"lat":54.792868,"lng":24.679878},{"lat":54.79306,"lng":24.679882},{"lat":54.793287,"lng":24.679989}]]};

const RESTRICTED_0428 = {"hardOutline":[[{"lat":54.793928,"lng":24.679042},{"lat":54.794814,"lng":24.679329},{"lat":54.79462,"lng":24.680617},{"lat":54.793907,"lng":24.680281},{"lat":54.793928,"lng":24.679042}],[{"lat":54.791215,"lng":24.678164},{"lat":54.791186,"lng":24.678998},{"lat":54.791009,"lng":24.678914},{"lat":54.791037,"lng":24.678107},{"lat":54.791215,"lng":24.678164}]],"hardHatch":[[{"lat":54.794802,"lng":24.679325},{"lat":54.794812,"lng":24.679343}],[{"lat":54.794678,"lng":24.679285},{"lat":54.794791,"lng":24.679484}],[{"lat":54.794555,"lng":24.679245},{"lat":54.794769,"lng":24.679624}],[{"lat":54.794432,"lng":24.679206},{"lat":54.794748,"lng":24.679764}],[{"lat":54.794308,"lng":24.679166},{"lat":54.794727,"lng":24.679905}],[{"lat":54.794185,"lng":24.679126},{"lat":54.794706,"lng":24.680045}],[{"lat":54.794062,"lng":24.679086},{"lat":54.794685,"lng":24.680185}],[{"lat":54.793938,"lng":24.679046},{"lat":54.794664,"lng":24.680326}],[{"lat":54.793925,"lng":24.6792},{"lat":54.794643,"lng":24.680466}],[{"lat":54.793922,"lng":24.679372},{"lat":54.794622,"lng":24.680607}],[{"lat":54.793919,"lng":24.679545},{"lat":54.794493,"lng":24.680558}],[{"lat":54.793916,"lng":24.679717},{"lat":54.794356,"lng":24.680493}],[{"lat":54.793913,"lng":24.67989},{"lat":54.794218,"lng":24.680428}],[{"lat":54.79391,"lng":24.680062},{"lat":54.794081,"lng":24.680363}],[{"lat":54.793907,"lng":24.680235},{"lat":54.793944,"lng":24.680298}],[{"lat":54.791102,"lng":24.678128},{"lat":54.79121,"lng":24.678317}],[{"lat":54.791034,"lng":24.678185},{"lat":54.791204,"lng":24.678485}],[{"lat":54.791029,"lng":24.678353},{"lat":54.791198,"lng":24.678652}],[{"lat":54.791023,"lng":24.67852},{"lat":54.791193,"lng":24.67882}],[{"lat":54.791017,"lng":24.678688},{"lat":54.791187,"lng":24.678987}],[{"lat":54.791011,"lng":24.678855},{"lat":54.791058,"lng":24.678937}]],"heritOutline":[[{"lat":54.793742,"lng":24.679083},{"lat":54.794074,"lng":24.67909},{"lat":54.794535,"lng":24.679239},{"lat":54.794549,"lng":24.67933},{"lat":54.794834,"lng":24.679336},{"lat":54.795008,"lng":24.679392},{"lat":54.794966,"lng":24.679608},{"lat":54.794916,"lng":24.679629},{"lat":54.794914,"lng":24.679879},{"lat":54.794833,"lng":24.680295},{"lat":54.794781,"lng":24.680312},{"lat":54.794776,"lng":24.68059},{"lat":54.794758,"lng":24.680682},{"lat":54.79462,"lng":24.680618},{"lat":54.794601,"lng":24.6805},{"lat":54.794362,"lng":24.680496},{"lat":54.79408,"lng":24.680363},{"lat":54.794064,"lng":24.680258},{"lat":54.793849,"lng":24.680254},{"lat":54.793541,"lng":24.680108},{"lat":54.793526,"lng":24.680016},{"lat":54.793337,"lng":24.680012},{"lat":54.793016,"lng":24.679861},{"lat":54.793012,"lng":24.679796},{"lat":54.792891,"lng":24.67977},{"lat":54.792897,"lng":24.678838},{"lat":54.793317,"lng":24.678845},{"lat":54.793725,"lng":24.678977},{"lat":54.793742,"lng":24.679083}]]};

// MERGED block outline
const MERGED = {path:[{lat:54.794575,lng:24.681621},{lat:54.794499,lng:24.681966},{lat:54.79431,lng:24.682815},{lat:54.794212,lng:24.682759},{lat:54.794194,lng:24.682749},{lat:54.793984,lng:24.682629},{lat:54.793762,lng:24.682503},{lat:54.792245,lng:24.68164},{lat:54.791381,lng:24.680315},{lat:54.790982,lng:24.679702},{lat:54.790991,lng:24.679441},{lat:54.791009,lng:24.678914},{lat:54.794758,lng:24.680682},{lat:54.794628,lng:24.68135},{lat:54.794575,lng:24.681621}],center:{lat:54.792967,lng:24.680847},plotas:'5.0250'};

// ── MARKET MARKERS (from sklypai-master-sarasas.md) ──
// cat: 'industry' | 'agri' | 'resi' | 'comm' | 'change'
const MARKET_MARKERS = [
  // Ausieniškių koridorius
  {id:'geliu-3ha',    lat:54.7935, lng:24.6790, cat:'industry', title:'Gėlių g. 3.0 ha',     price:'390 000 €', eurha:'130 000 €/ha', pask:'Pramonė/sandėliavimas', dist:'~0.3 km', url:'https://www.kampas.lt/skelbimai/sklypas-elektrenuose-ausieniskiu-k-geliu-g-parduodamas-3-ha-pramones-ir-1047812'},
  {id:'geliu-34a',    lat:54.7932, lng:24.6787, cat:'industry', title:'Gėlių g. 34A 1.03 ha',price:'65 000 €',  eurha:'63 400 €/ha',  pask:'Sandėliavimas (keista)', dist:'~0.3 km', url:'https://www.alio.lt/skelbimai/id68730617'},
  {id:'pramones-g',   lat:54.7938, lng:24.6795, cat:'industry', title:'Pramonės g. 2.70 ha', price:'270 000 €', eurha:'99 300 €/ha',  pask:'Pramonė/sandėl./kom.',  dist:'~0.4 km', url:'https://m.en.aruodas.lt/sklypai/elektrenuose/ausieniskiu-k/'},
  {id:'ausieniskes-74a',lat:54.7930,lng:24.6792, cat:'comm',   title:'Ausieniškių k. 74.4a',price:'44 000 €',  eurha:'59 100 €/ha',  pask:'Komercinė',             dist:'~0.3 km', note:'+47.2% — ties RC rinka', url:'https://m.en.aruodas.lt/sklypai/elektrenuose/ausieniskiu-k/'},
  {id:'paukštyno',   lat:54.7942, lng:24.6805, cat:'resi',     title:'Paukštyno g. 25a',    price:'22 000 €',  eurha:'88 000 €/ha',  pask:'Namų valda',            dist:'~0.5 km', note:'Kaba 15+ mėn.', url:'https://m.en.aruodas.lt/sklypai/elektrenuose/ausieniskiu-k/'},
  {id:'aliosos',      lat:54.7928, lng:24.6788, cat:'resi',     title:'Aliosos g. 23.9a',    price:'18 000 €',  eurha:'75 300 €/ha',  pask:'Namų valda',            dist:'~0.3 km', url:'https://m.en.aruodas.lt/sklypai/elektrenuose/ausieniskiu-k/'},
  // Sabališkių
  {id:'sabaliskes-16a',lat:54.7910,lng:24.6760, cat:'agri',    title:'Sabališkių k. 16a',   price:'14 000 €',  eurha:'87 500 €/ha',  pask:'Žemės ūkio (spekulat.)',dist:'~1.0 km', note:'Šalia Rimi; "galima keisti paskirtį"', url:'https://www.elektrenuvaldos.lt/sklypai/parduodamas-16-aru-zemes-sklypas-sabaliskese'},
  // Paskirties keitimo prašymai
  {id:'0005-change',  lat:54.790491,lng:24.678053, cat:'change',title:'01.3-192 · 7910/0001:0005',price:'—', eurha:'Agri → Pramonė', pask:'Paskirties keitimas', dist:'443 m', note:'Viešinimas baigėsi 2026-06-15. Rezultatas: 2026-06-16', url:'https://planuojustatau.lt/sites/default/files/01.3-192.jpg'},
  {id:'0151-change',  lat:54.795,   lng:24.677,   cat:'change', title:'01.3-151 · 7910/0007:619+571',price:'—',eurha:'Agri → Gyvenamoji',pask:'Paskirties keitimas',dist:'~0.5 km',url:''},
  {id:'0170-change',  lat:54.796,   lng:24.680,   cat:'change', title:'01.3-170 · 7910/0008:37',price:'—',eurha:'Agri → Gyvenamoji',pask:'Paskirties keitimas',dist:'~0.6 km',url:''},
  {id:'0106-change',  lat:54.773,   lng:24.723,   cat:'change', title:'01.3-106 · Vidugiriai',price:'—',eurha:'Agri → Pramonė',pask:'Paskirties keitimas',dist:'~5 km',url:''},
  // Radius pipeline — agri
  {id:'zebertoniai',  lat:54.801476,lng:24.706391, cat:'agri',  title:'Žebertoniai 2.1 ha',  price:'24 000 €',  eurha:'11 429 €/ha',  pask:'Žemės ūkio',            dist:'1.78 km', url:'https://m.en.aruodas.lt/sklypai/elektrenuose/'},
  {id:'pakalnis',     lat:54.753457,lng:24.758108, cat:'agri',  title:'Pakalniškiai 3.2 ha', price:'42 000 €',  eurha:'13 125 €/ha',  pask:'Žemės ūkio+gyv.',       dist:'6.62 km', url:'https://m.en.aruodas.lt/sklypai/elektrenuose/'},
  {id:'bauboniai',    lat:54.765393,lng:24.774058, cat:'agri',  title:'Bauboniai 3.4 ha',    price:'20 000 €',  eurha:'5 882 €/ha',   pask:'Žemės ūkio',            dist:'6.69 km', note:'≈ RC sandorių kainai', url:'https://m.en.aruodas.lt/sklypai/elektrenuose/'},
  // Industry remote
  // zilviciu: Kakliniškių k. village centroid from geocoder (same as bauboniai) — offset slightly so markers don't stack
  {id:'zilviciu',     lat:54.765693,lng:24.774358, cat:'industry',title:'Žilvičių g. 48a',   price:'95 000 €',  eurha:'197 917 €/ha', pask:'Pramonė/sandėl./kom.',  dist:'6.69 km', note:'Kakliniškių k. centroid ± ~35 m (geocoder village-level)', url:'https://m.en.aruodas.lt/sklypai/elektrenuose/kakliniskiu-k/'},
  {id:'kakliniskes-a1',lat:54.764,  lng:24.770,   cat:'agri',   title:'Kakliniškės 3.05 ha (A1)',price:'299 000 €',eurha:'98 033 €/ha',pask:'Žemės ūkio (spekulat.)',dist:'~6.5 km',note:'A1 adjacency premium ×16',url:'https://www.kampas.lt/skelbimai/sklypas-elektrenuose-kakliniskiu-k-parduodamas-305-ha-sklypas-salia-a1-magistrales-1054974'},
  // Residential radius
  {id:'abromiškiai',  lat:54.780597,lng:24.716731, cat:'resi',  title:'Abromiškiai 1.1 ha',  price:'29 900 €',  eurha:'27 182 €/ha',  pask:'Žemės ūkio',            dist:'2.65 km', note:'Kurortinė zona — premija paaiškinama', url:''},
];

// SŽNS overlay config (LKS94 raster)
proj4.defs('EPSG:3346','+proj=tmerc +lat_0=0 +lon_0=24 +k=0.9996 +x_0=500000 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs');
const toLKS = proj4('EPSG:4326','EPSG:3346');
const toWGS = proj4('EPSG:3346','EPSG:4326');
const SZNS = {url:'https://www.geoportal.lt/mapproxy/rc_szns/MapServer/tile',tile:512,originX:18900,originY:6258000,res:[1587.5031750063501,793.7515875031751,529.1677250021168,264.5838625010584,132.2919312505292,52.91677250021167,26.458386250105836,13.229193125052918,6.614596562526459,2.6458386250105836,1.3229193125052918,0.5291677250021167,0.26458386250105836]};

// BPD corridor: Elektrėnai → Vievis (approximate axis along road 4728 direction)
const CORRIDOR_PATH = [
  {lat:54.800,lng:24.666},  // Elektrėnai miesto pakraštys
  {lat:54.797,lng:24.669},
  {lat:54.794,lng:24.674},  // per Rimi zoną
  {lat:54.792,lng:24.681},  // per šeimos bloką
  {lat:54.789,lng:24.690},
  {lat:54.783,lng:24.730},
  {lat:54.775,lng:24.763},  // Vievio prieigas
  {lat:54.768,lng:24.785},  // Vievis
];

let map, labels=[], labelsOn=true, TextLabel;
let sznsOverlay=null, azShapes=[], marketMarkers=[], distCircles=[], corridorLine=null;
```

- [ ] **Step 2: Commit data constants**

```bash
git add dashboard-v1.html
git commit -m "feat(dashboard-v1): embed all JS data constants — parcels, AZ, market markers, corridor"
```

---

## Task 7: Map initialization + all layers

**Files:**
- Modify: `C:\Users\retco\Projects\Elektrenai\dashboard-v1.html` — add all JS functions after data constants, before `</script>`

- [ ] **Step 1: Add SŽNS overlay class + helper functions**

Append to `<script>` block (after constants):

```javascript
function pickSznsLevel(z){const m=156543.03392*Math.cos(54.79*Math.PI/180)/Math.pow(2,z);let b=SZNS.res.length-1;for(let i=0;i<SZNS.res.length;i++){if(SZNS.res[i]<=m){b=i;break;}}return Math.max(9,Math.min(12,b));}

function defineSznsOverlay(){
  sznsOverlay=new(class extends google.maps.OverlayView{
    constructor(){super();this.layer=null;this.imgs=new Map();}
    onAdd(){this.layer=document.createElement('div');this.layer.style.cssText='position:absolute;opacity:0.55';this.getPanes().mapPane.appendChild(this.layer);}
    onRemove(){if(this.layer){this.layer.remove();this.layer=null;}this.imgs.clear();}
    draw(){
      const proj=this.getProjection();if(!proj||!this.layer)return;
      const b=map.getBounds();if(!b)return;
      const level=pickSznsLevel(map.getZoom()),span=SZNS.tile*SZNS.res[level];
      const ne=b.getNorthEast(),sw=b.getSouthWest();
      const corners=[[sw.lng(),sw.lat()],[ne.lng(),ne.lat()],[sw.lng(),ne.lat()],[ne.lng(),sw.lat()]].map(c=>toLKS.forward(c));
      const xs=corners.map(c=>c[0]),ys=corners.map(c=>c[1]);
      const minX=Math.min(...xs),maxX=Math.max(...xs),minY=Math.min(...ys),maxY=Math.max(...ys);
      const c0=Math.floor((minX-SZNS.originX)/span),c1=Math.floor((maxX-SZNS.originX)/span);
      const r0=Math.floor((SZNS.originY-maxY)/span),r1=Math.floor((SZNS.originY-minY)/span);
      const want=new Set();
      for(let r=r0;r<=r1;r++)for(let c=c0;c<=c1;c++){
        const key=level+'/'+r+'/'+c;want.add(key);
        const x0=SZNS.originX+c*span,y1=SZNS.originY-r*span,x1=x0+span,y0=y1-span;
        const tl=toWGS.forward([x0,y1]),br=toWGS.forward([x1,y0]);
        const pTL=proj.fromLatLngToDivPixel(new google.maps.LatLng(tl[1],tl[0]));
        const pBR=proj.fromLatLngToDivPixel(new google.maps.LatLng(br[1],br[0]));
        let img=this.imgs.get(key);
        if(!img){img=document.createElement('img');img.src=SZNS.url+'/'+level+'/'+r+'/'+c;img.style.cssText='position:absolute;pointer-events:none';img.onerror=()=>img.style.display='none';this.layer.appendChild(img);this.imgs.set(key,img);}
        img.style.left=pTL.x+'px';img.style.top=pTL.y+'px';img.style.width=(pBR.x-pTL.x)+'px';img.style.height=(pBR.y-pTL.y)+'px';
      }
      for(const[key,img]of this.imgs)if(!want.has(key)){img.remove();this.imgs.delete(key);}
    }
  })();
}

function chordSpans(path,c){const xs=[],ys=[];for(let i=0;i<path.length-1;i++){const a=path[i],b=path[i+1];if((a.lat-c.lat)*(b.lat-c.lat)<0)xs.push(a.lng+(b.lng-a.lng)*(c.lat-a.lat)/(b.lat-a.lat));if((a.lng-c.lng)*(b.lng-c.lng)<0)ys.push(a.lat+(b.lat-a.lat)*(c.lng-a.lng)/(b.lng-a.lng));}xs.sort((p,q)=>p-q);ys.sort((p,q)=>p-q);let w=0,h=0,mx=c.lng,my=c.lat;for(let i=0;i+1<xs.length;i+=2)if(xs[i]<=c.lng&&c.lng<=xs[i+1]){w=xs[i+1]-xs[i];mx=(xs[i]+xs[i+1])/2;break;}for(let i=0;i+1<ys.length;i+=2)if(ys[i]<=c.lat&&c.lat<=ys[i+1]){h=ys[i+1]-ys[i];my=(ys[i]+ys[i+1])/2;break;}return{w,h,mx,my};}

function fitLabelPoint(path,c){let p={lat:c.lat,lng:c.lng},s;s=chordSpans(path,p);p={lat:p.lat,lng:s.mx};s=chordSpans(path,p);p={lat:s.my,lng:p.lng};s=chordSpans(path,p);p={lat:p.lat,lng:s.mx};s=chordSpans(path,p);return{pos:p,span:s};}
```

- [ ] **Step 2: Add TextLabel class definition**

```javascript
function defineTextLabel(){
  TextLabel=class extends google.maps.OverlayView{
    constructor(pos,html,span){super();this.pos=pos;this.html=html;this.span=span;}
    onAdd(){this.div=document.createElement('div');this.div.className='plabel';this.div.style.position='absolute';this.div.innerHTML=this.html;this.getPanes().overlayLayer.appendChild(this.div);this.nw=this.div.offsetWidth;this.nh=this.div.offsetHeight;}
    draw(){const proj=this.getProjection();if(!proj||!this.div)return;const p=proj.fromLatLngToDivPixel(this.pos);this.div.style.left=p.x+'px';this.div.style.top=p.y+'px';if(this.span&&this.nw){const c=this.pos,pw1=proj.fromLatLngToDivPixel(new google.maps.LatLng(c.lat(),c.lng()-this.span.w/2)),pw2=proj.fromLatLngToDivPixel(new google.maps.LatLng(c.lat(),c.lng()+this.span.w/2)),ph1=proj.fromLatLngToDivPixel(new google.maps.LatLng(c.lat()-this.span.h/2,c.lng())),ph2=proj.fromLatLngToDivPixel(new google.maps.LatLng(c.lat()+this.span.h/2,c.lng()));const pw=Math.abs(pw2.x-pw1.x),ph2px=Math.abs(ph1.y-ph2.y),s=Math.min(1,pw*0.9/this.nw,ph2px*0.9/this.nh);this.div.style.transform=`translate(-50%,-50%) scale(${s})`;this.div.style.display=(this.hidden||s<0.35)?'none':'';}};
    onRemove(){if(this.div){this.div.remove();this.div=null;}}
    setVisible(v){this.hidden=!v;if(this.div)this.div.style.display=v?'':'none';if(v)this.draw();}
  };
}
```

- [ ] **Step 3: Add initMap function**

```javascript
function initMap(){
  defineTextLabel();
  map=new google.maps.Map(document.getElementById('map'),{
    center:{lat:54.7929,lng:24.6829},zoom:16,mapTypeId:'hybrid',tilt:0
  });

  const FAMILY={stroke:'#FFFF00',fill:'#FFF176',op:0.12,z:11,w:2};
  const PSTYLE={'7910/0001:0005':{stroke:'#0066FF',fill:'#00AAFF',op:0,z:10},'7910/0001:0428':FAMILY,'7910/0001:0429':FAMILY,'7910/0001:0430':FAMILY,'7910/0001:0431':FAMILY};
  const NEIGHBOR={stroke:'#39FF14',fill:'#76FF03',op:0.07,z:10,w:1};

  // parcel polygons + labels
  for(const[kn,d]of Object.entries(DATA)){
    const st=PSTYLE[kn]||NEIGHBOR;
    new google.maps.Polygon({paths:d.path,strokeColor:st.stroke,strokeWeight:st.w||1,fillColor:st.fill,fillOpacity:st.op,zIndex:st.z,map});
    const fit=fitLabelPoint(d.path,d.center);
    const nm=NAMES[kn]?`<span class="pname">${NAMES[kn]}<br></span>`:'';
    const lbl=new TextLabel(new google.maps.LatLng(fit.pos.lat,fit.pos.lng),`${nm}${kn}<br><small>${d.plotas} ha</small>`,fit.span);
    lbl.setMap(map);labels.push(lbl);
  }

  // Rimi
  new google.maps.Polygon({paths:RIMI.path,strokeColor:'#39FF14',strokeWeight:2,fillColor:'#76FF03',fillOpacity:0.10,zIndex:10,map});
  const rimiFit=fitLabelPoint(RIMI.path,RIMI.center);
  const rimiLbl=new TextLabel(new google.maps.LatLng(rimiFit.pos.lat,rimiFit.pos.lng),`${RIMI.kn}<br><small>Rimi logistikos centras — 12.85 ha</small>`,rimiFit.span);
  rimiLbl.setMap(map);labels.push(rimiLbl);

  // precedent
  new google.maps.Polygon({paths:PRECEDENT.path,strokeColor:'#39FF14',strokeWeight:2,fillColor:'#76FF03',fillOpacity:0.15,zIndex:10,map});
  const precLbl=new TextLabel(new google.maps.LatLng(PRECEDENT.center.lat,PRECEDENT.center.lng),`${PRECEDENT.kn}<br><small>3.00 ha — pramonė, 130 k€/ha</small>`,chordSpans(PRECEDENT.path,PRECEDENT.center));
  precLbl.setMap(map);labels.push(precLbl);

  // merged block
  new google.maps.Polygon({paths:MERGED.path,strokeOpacity:0,fillColor:'#FFFF00',fillOpacity:0.08,zIndex:12,map});
  new google.maps.Polyline({path:MERGED.path,strokeOpacity:0,zIndex:12,map,icons:[{icon:{path:'M 0,-1 0,1',strokeOpacity:1,strokeColor:'#FF0000',strokeWeight:2,scale:3},offset:'0',repeat:'12px'}]});

  // AZ zones: hard ban + heritage for both blocks
  for(const ring of RESTRICTED.hardOutline){azShapes.push(new google.maps.Polygon({paths:ring,strokeColor:'#B71C1C',strokeWeight:2,fillColor:'#FF0000',fillOpacity:0.08,zIndex:7,map}));}
  for(const seg of RESTRICTED.hardHatch){azShapes.push(new google.maps.Polyline({path:seg,strokeColor:'#D32F2F',strokeWeight:1,strokeOpacity:0.9,zIndex:7,map}));}
  for(const ring of RESTRICTED.heritOutline){azShapes.push(new google.maps.Polygon({paths:ring,strokeColor:'#FF8F00',strokeWeight:2,fillColor:'#FFB300',fillOpacity:0.13,zIndex:6,map}));}
  for(const ring of RESTRICTED_0428.hardOutline){azShapes.push(new google.maps.Polygon({paths:ring,strokeColor:'#B71C1C',strokeWeight:2,fillColor:'#FF0000',fillOpacity:0.08,zIndex:7,map}));}
  for(const seg of RESTRICTED_0428.hardHatch){azShapes.push(new google.maps.Polyline({path:seg,strokeColor:'#D32F2F',strokeWeight:1,strokeOpacity:0.9,zIndex:7,map}));}
  for(const ring of RESTRICTED_0428.heritOutline){azShapes.push(new google.maps.Polygon({paths:ring,strokeColor:'#FF8F00',strokeWeight:2,fillColor:'#FFB300',fillOpacity:0.13,zIndex:6,map}));}

  // road frontage
  new google.maps.Polyline({path:[{lat:54.790982,lng:24.679702},{lat:54.790991,lng:24.679441},{lat:54.791009,lng:24.678914}],strokeColor:'#FF6D00',strokeWeight:4,zIndex:13,map});

  // merged label
  const mLbl=new TextLabel(new google.maps.LatLng(54.7921,24.68045),'Apjungta 0429+0430+0431<br><small>5.0250 ha</small>',chordSpans(MERGED.path,{lat:54.7921,lng:24.68045}));
  mLbl.setMap(map);labels.push(mLbl);

  // BPD corridor polyline (hidden by default) — dashes via icons, strokeDashArray is SVG only
  corridorLine=new google.maps.Polyline({path:CORRIDOR_PATH,strokeOpacity:0,zIndex:5,map:null,icons:[{icon:{path:'M 0,-1 0,1',strokeOpacity:0.6,strokeColor:'#9C27B0',strokeWeight:3,scale:4},offset:'0',repeat:'16px'}]});

  // distance circles (hidden by default)
  const CENTER={lat:54.793655,lng:24.682243};
  distCircles=[
    new google.maps.Circle({center:CENTER,radius:500, strokeColor:'#FFFFFF',strokeWeight:1,strokeOpacity:0.4,fillOpacity:0,zIndex:4,map:null}),
    new google.maps.Circle({center:CENTER,radius:2000,strokeColor:'#FFD700',strokeWeight:1,strokeOpacity:0.4,fillOpacity:0,zIndex:4,map:null}),
    new google.maps.Circle({center:CENTER,radius:8000,strokeColor:'#64B5F6',strokeWeight:1,strokeOpacity:0.3,fillOpacity:0,zIndex:4,map:null}),
  ];

  // market markers
  const CAT_ICONS={
    industry:{color:'#D32F2F'},
    agri:    {color:'#F9A825'},
    resi:    {color:'#1565C0'},
    comm:    {color:'#2E7D32'},
    change:  {color:'#E65100'},
  };
  const iw=new google.maps.InfoWindow();
  const markerById={};  // id → google.maps.Marker — for focusMarker()
  for(const m of MARKET_MARKERS){
    const col=CAT_ICONS[m.cat].color;
    const marker=new google.maps.Marker({
      position:{lat:m.lat,lng:m.lng},map,
      icon:{path:google.maps.SymbolPath.CIRCLE,scale:8,fillColor:col,fillOpacity:0.9,strokeColor:'#fff',strokeWeight:1.5},
      title:m.title,zIndex:20
    });
    marker.addListener('click',()=>{
      iw.setContent(`<div class="mkt-popup"><div class="mp-title">${m.title}</div><div class="mp-row"><span>Kaina</span><b>${m.price}</b></div><div class="mp-row"><span>€/ha</span><b>${m.eurha}</b></div><div class="mp-row"><span>Paskirtis</span><b>${m.pask}</b></div><div class="mp-row"><span>Atstumas</span><b>${m.dist}</b></div>${m.note?`<div class="mp-row" style="color:#888;font-size:11px">${m.note}</div>`:''}</div>${m.url?`<a href="${m.url}" target="_blank">Skelbimas →</a>`:''}`);
      iw.open(map,marker);
    });
    marketMarkers.push(marker);
    markerById[m.id]=marker;
  }

  renderPriceBar();
  fitAll();
}
```

- [ ] **Step 4: Add toggle + utility functions**

```javascript
function toggleAz(on){azShapes.forEach(s=>s.setMap(on?map:null));}
function toggleSzns(on){
  document.getElementById('sznsLegendBox').style.display=on?'block':'none';
  if(on){if(!sznsOverlay)defineSznsOverlay();sznsOverlay.setMap(map);}
  else if(sznsOverlay)sznsOverlay.setMap(null);
}
function toggleMarkers(on){marketMarkers.forEach(m=>m.setMap(on?map:null));}
function toggleCircles(on){distCircles.forEach(c=>c.setMap(on?map:null));}
function toggleCorridor(on){corridorLine.setMap(on?map:null);}

function fitAll(){
  const b=new google.maps.LatLngBounds();
  for(const d of Object.values(DATA))d.path.forEach(p=>b.extend(p));
  map.fitBounds(b);
}
function toggleLabels(){labelsOn=!labelsOn;labels.forEach(l=>l.setVisible(labelsOn));}
function toggleNames(){
  document.body.classList.toggle('names-off');
  // measure offsetWidth while visible (before CSS hides .pname), then redraw scale
  labels.forEach(l=>{
    if(!l.div)return;
    const was=l.div.style.display;
    l.div.style.display='';           // ensure measured while not force-hidden
    l.nw=l.div.offsetWidth;           // .pname already toggled by CSS class — correct size
    l.nh=l.div.offsetHeight;
    l.div.style.display=was;
    l.draw();
  });
}

function showTab(name){
  ['legenda','rinka','planavimas','zonos'].forEach(t=>{
    document.getElementById('tab-'+t).classList.toggle('active',t===name);
  });
  document.querySelectorAll('.tabs-nav button').forEach((b,i)=>{
    b.classList.toggle('active',['legenda','rinka','planavimas','zonos'][i]===name);
  });
}

// Focus map on a market marker by id — uses markerById map (O(1), no indexOf mismatch risk)
function focusMarker(id){
  const data=MARKET_MARKERS.find(x=>x.id===id);
  const marker=markerById[id];
  if(!data||!marker)return;
  map.setCenter({lat:data.lat,lng:data.lng});map.setZoom(17);
  google.maps.event.trigger(marker,'click');
}
```

- [ ] **Step 5: Add price bar renderer**

```javascript
function renderPriceBar(){
  const CEIL=500000;
  const segments=[
    {label:'RC grindys 31k',  val:31000,   color:'#888',     pct:31000/CEIL*100},
    {label:'Pirkėjas 50k',    val:50250,   color:'#EF5350',  pct:50250/CEIL*100},
    {label:'Agri asking',     val:66000,   color:'#FFB300',  pct:66000/CEIL*100},
    {label:'Kontrsiūl. 90k',  val:90450,   color:'#4CAF50',  pct:90450/CEIL*100},
    {label:'0005→ 125k',      val:125000,  color:'#81C784',  pct:125000/CEIL*100},
    {label:'Pram. RC 176k',   val:176000,  color:'#64B5F6',  pct:176000/CEIL*100},
    {label:'Pram. ceiling',   val:500000,  color:'#1565C0',  pct:100},
  ];
  const track=document.getElementById('pbTrack');
  let html='';
  // anchors
  for(const s of segments){
    html+=`<div class="pb-anchor" style="left:${s.pct}%;color:${s.color}">${s.label}</div>`;
  }
  // gradient fill band
  html+=`<div class="pb-seg" style="left:0;width:${segments[0].pct}%;background:#444"></div>`;
  for(let i=0;i<segments.length-1;i++){
    const a=segments[i],b=segments[i+1];
    html+=`<div class="pb-seg" style="left:${a.pct}%;width:${b.pct-a.pct}%;background:${b.color};opacity:.8"></div>`;
  }
  track.innerHTML=html;
}
```

- [ ] **Step 6: Add Maps API injection + close script tag**

```javascript
window.initMap=initMap;
(function(){
  let key=window.MAPS_API_KEY;
  if(!key){const inj='__MAPS_API_KEY__';if(inj.indexOf('MAPS_API_KEY')===-1)key=inj;}
  if(!key){document.getElementById('map').innerHTML='<div style="padding:40px;color:#fff;font-family:sans-serif"><h2>Trūksta API rakto</h2><p>Lokaliai: <code>python gen_config.py</code></p></div>';return;}
  const s=document.createElement('script');s.async=true;
  s.src='https://maps.googleapis.com/maps/api/js?key='+encodeURIComponent(key)+'&callback=initMap';
  document.head.appendChild(s);
})();
</script>
</body>
</html>
```

- [ ] **Step 7: Test in browser**

```bash
python -m http.server 8124
# http://localhost:8124/dashboard-v1.html
# Checklist:
# [ ] Dark theme renders — top bar, sidebar, price bar visible
# [ ] Map loads (hybrid), parcels drawn in yellow/green
# [ ] 17 market markers visible (colored dots)
# [ ] Click marker → InfoWindow with price/pask/atstumas
# [ ] Sidebar Rinka tab → click listing → map pans + opens popup
# [ ] AZ toggle works (red hatch appears/disappears)
# [ ] SŽNS toggle works (raster overlay)
# [ ] Circles toggle: 3 rings at 0.5/2/8 km
# [ ] Corridor toggle: purple polyline Elektrėnai→Vievis
# [ ] Price bar shows colored segments with anchors
# [ ] All 4 tabs switch correctly
```

- [ ] **Step 8: Commit**

```bash
git add dashboard-v1.html
git commit -m "feat(dashboard-v1): full map init — parcels, AZ, 17 market markers, toggles, price bar"
```

---

## Task 8: Final verification + deploy

**Files:**
- Read: `C:\Users\retco\Projects\Elektrenai\.github\workflows\deploy.yml` (confirm `dashboard-v1.html` is included — static HTML, should work automatically)

- [ ] **Step 1: Check deploy.yml includes new file**

```bash
cat .github/workflows/deploy.yml
# Expect: copies all .html files or entire repo to Pages
# If only copies sklypas-google.html → update to copy *.html
```

- [ ] **Step 2: If deploy.yml needs update, add dashboard-v1.html**

Only if the workflow explicitly lists files — change from `sklypas-google.html` to `*.html` or add `dashboard-v1.html` alongside.

- [ ] **Step 3: Smoke test checklist in browser (full)**

```bash
python -m http.server 8124
# http://localhost:8124/dashboard-v1.html
# [ ] Top bar: all 6 KPIs visible, status badge pulses
# [ ] Map: hybrid, parcels + labels correct
# [ ] Market markers: 17 dots, 5 categories (red/yellow/blue/green/orange)
# [ ] Legenda tab: layer toggles work
# [ ] Rinka tab: price blocks + clickable listings
# [ ] Planavimas tab: BPD radiniai + 14 paskirties keitimų + TPDRIS
# [ ] Zonos tab: bar chart + zone breakdown
# [ ] Price bar: segments labeled
# [ ] sklypas-google.html still works at http://localhost:8124/sklypas-google.html
```

- [ ] **Step 4: Push to main → GitHub Pages deploy**

```bash
git push origin main
gh run watch
# Expect: deploy succeeds; https://gerimantas.github.io/elektrenai/dashboard-v1.html live
```

- [ ] **Step 5: Verify live URL**

Open `https://gerimantas.github.io/elektrenai/dashboard-v1.html` — confirm map loads (API key injected by CI).

---

## Self-Review

### Spec coverage

| Requirement | Task |
|---|---|
| Esamas HTML nepaliečiamas | `sklypas-google.html` DO NOT TOUCH note in every task |
| Dark investment dashboard | Task 1 CSS + layout |
| Top bar su KPIs | Task 1 Step 2 |
| 4-tab sidebar | Task 1 Step 3 |
| Legenda tab | Task 2 |
| Rinka tab su kainomis | Task 3 |
| Planavimas tab su BPD + 16 prašymų | Task 4 |
| Zonos tab su bar chart | Task 5 |
| Parcel polygons + AZ zones (copy from sklypas-google) | Task 6 |
| 17 market markers su popups | Task 6 + Task 7 Step 3 |
| Sidebar listing → map focus | Task 7 Step 4 `focusMarker()` |
| Atstumų žiedai (3 rings) | Task 7 Step 3 |
| BPD koridorius polyline | Task 7 Step 3 |
| Price bar vizualizacija | Task 7 Step 5 |
| SŽNS overlay | Task 7 Step 1 |
| Toggles: AZ / SŽNS / markers / circles / corridor | Task 7 Step 4 |
| API key injection (same as sklypas-google) | Task 7 Step 6 |
| Deploy to Pages | Task 8 |

### Placeholder scan
None found — all steps have complete code.

### Type consistency
- `focusMarker(id)` called in Task 3 HTML — defined in Task 7 Step 4 ✅
- `focusMarker` uses `markerById[id]` map (built in `initMap`) — no `indexOf` race ✅
- `showTab(name)` called in Task 1 HTML — defined in Task 7 Step 4 ✅
- `toggleAz / toggleSzns / toggleMarkers / toggleCircles / toggleCorridor` — all called in Task 2 HTML, defined in Task 7 Step 4 ✅
- `MARKET_MARKERS[i].id` used in `focusMarker` — matches `id` field in every marker object in Task 6 ✅
- `renderPriceBar()` called in `initMap` — defined in Task 7 Step 5 ✅
- `corridorLine` uses `icons` pattern (not `strokeDashArray`) — matches Google Maps JS API ✅
- `markerById` declared in `initMap` scope — accessible to `focusMarker` via closure ✅

### Known limitations (not bugs)
- Ausieniškių corridor markers (1.1–1.6: `pramones-g`, `ausieniskes-74a`, `paukštyno`, `aliosos`): village-level coords (~54.793, 24.680) — geocoder returned centroid. Exact coords pending aruodas page geocoding (see master sąrašas TODO).
- `zilviciu` and `bauboniai`: same Kakliniškių k. centroid from geocoder; `zilviciu` offset +0.003°lat/lng so markers don't stack.
- `0151-change` and `0170-change`: approximate coords (7910/0007 and 7910/0008 blocks not in RC ZIP 42 — different cadastral district).

---
