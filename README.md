# Elektrėnai — sklypo žemėlapis

Interaktyvus žemės sklypo **Nr. 4400-1563-8352** (kadastrinis **7910/0001:0431**, Ausieniškių k., Elektrėnų sav.) žemėlapis su kaimyniniais sklypais.

🗺️ **Žiūrėti:** https://gerimantas.github.io/elektrenai/

## Kas rodoma

- 🔴 **7910/0001:0431** — pagrindinis sklypas (1.6750 ha, žemės ūkio)
- 🔵 **7910/0001:0005** — netoliese vykstantis paskirties keitimas (ž.ū. → pramonė/sandėliavimas, vieša apžiūra iki 2026-06-15)
- 🟡 6 besiribojantys kaimyniniai sklypai

Kiekvienas sklypas pažymėtas pilnu kadastro numeriu + plotu. Mygtukai: Satellite / Hybrid / Roadmap / Centruoti / Label on/off. Info langas suskleidžiamas.

## Duomenų šaltinis

Sklypų ribos — **Registrų centro atviri duomenys** ([data.gov.lt rinkinys 2831](https://data.gov.lt/datasets/2831/), CC BY 4.0, EPSG:3346/LKS94). Geometrija patikrinta prieš oficialų RC žemėlapį — ploto skirtumas 0.00%.

Savininkų duomenų nėra (asmens duomenys, GDPR — neviešinami).

## Techninė info

- Statinis HTML + Google Maps JavaScript API
- Hostinamas per GitHub Pages (deploy per GitHub Actions)
- API raktas įterpiamas deploy metu iš repo secret, niekada nekomituojamas plain-text
- Raktas apribotas pagal HTTP referrer (tik šis domenas)

### Lokalus paleidimas

```bash
cp .env.example .env        # įrašyk savo MAPS_API_KEY
python gen_config.py        # sugeneruoja config.js
python -m http.server       # http://localhost:8000/sklypas-google.html
```

`file://` (dvigubu paspaudimu) neveiks — Google raktas apribotas localhost + github.io referreriais.
