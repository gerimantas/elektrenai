# Elektrėnai — 7910/0001 bloko žemėlapis

Šeimos žemės sklypų **7910/0001:0428–0431** (Kakliniškių k., Elektrėnų sav.) tyrimo
ir sprendimo įrankis: sklypų ribos, užstatymo apribojimai, aplinkinė rinka ir
surinktos tyrimo išvados vienoje vietoje.

🗺️ **Žiūrėti:** https://gerimantas.github.io/elektrenai/

Duomenys atnaujinti **2026-08-10**.

## Trys vaizdai

Viršutiniame meniu — **Žemėlapis**, **Rinka**, **Tyrimas**.

### Žemėlapis

Palydovinis vaizdas su sklypų ribomis. Kiekvienas sklypas pažymėtas kadastro
numeriu ir plotu.

- 🟡 **šeimos sklypai 0428–0431** — 0429+0430+0431 sudaro apjungtą **5.0250 ha**
  bloką; 0428 (3.0500 ha) greta
- 🟥 **statybų draudimo AZ** — dujotiekiai 25 m + kelias 20 m; laisva statybai
  lieka **3.39 ha**
- 🟧 **paveldo AZ 119** — reikalingas KPD derinimas; zonos persidengia
- 🔵 **7910/0001:0005** — gretimas paskirties keitimo prašymas (0.3141 ha)
- 🟢 **7910/0001:0922** — Rimi logistikos centras (12.85 ha)
- 🟢 kiti kaimyniniai sklypai

Valdikliai: Centruoti · Legenda · Parduodami · Label · Vardai.
**Parduodami** uždeda rinkos sluoksnį — sklypus reikia atitolinti, jie išsibarstę
iki ~17 km.

### Rinka

**124 skelbimai** Elektrėnų sav. (aruodas.lt, 2026-08-10): **53 su tiksliomis RC
ribomis**, likę 72 — kaimų taškais. Rūšiuojama ir filtruojama pagal atstumą,
paskirtį, plotą; „→ rodyti" nuveda į sklypą žemėlapyje.

### Tyrimas

Surinktos išvados su šaltiniais — kas pasikeitė nuo praėjusio skenavimo, RC
masinio vertinimo sandoriai, bloko vertė, paskirties keitimai apylinkėje,
įvažiavimas iš kelio 4728, užstatymo apribojimai.

## Duomenų šaltiniai

- **Sklypų ribos** — Registrų centro atviri duomenys
  ([data.gov.lt rinkinys 2831](https://data.gov.lt/datasets/2831/), CC BY 4.0,
  EPSG:3346/LKS94). Geometrija patikrinta prieš oficialų RC žemėlapį — ploto
  skirtumas 0.00%.
- **Rinkos kainos** — aruodas.lt skenavimas.
- **Apsaugos zonos** — SŽNS rastras + statutiniai pločiai (vektoriai neprieinami).

Savininkų duomenų nėra (asmens duomenys, GDPR — neviešinami). Sklypų vardai
mygtuke „Vardai" — tik šeimos vidiniam naudojimui.

## Techninė info

- Statinis HTML + Google Maps JavaScript API (hybrid vaizdas)
- Hostinama per GitHub Pages, deploy per GitHub Actions
- API raktas įterpiamas deploy metu iš `MAPS_API_KEY` repo secret, niekada
  nekomituojamas plain-text
- Raktas apribotas pagal HTTP referrer (tik šis domenas)
- Publikuojamas tik sugeneruotas `_site/index.html` — tyrimo dokumentai
  (`CONTEXT.md`, `TYRIMO-ISVADOS.md`, `.planning/`) neserveriuojami

### Lokalus paleidimas

```bash
cp .env.example .env        # įrašyk savo MAPS_API_KEY
python gen_config.py        # sugeneruoja config.js (git-ignored)
python -m http.server 8123  # http://localhost:8123/sklypas-google.html
```

`file://` (dvigubu paspaudimu) neveiks — Google raktas apribotas localhost +
github.io referreriais.
