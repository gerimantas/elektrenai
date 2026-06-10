# Žemės sklypai — Elektrėnų sav.

## Sklypas Nr. 4400-1563-8352

| Laukas | Duomenys |
|--------|----------|
| **Unikalus Nr. (NTR)** | 4400-1563-8352 |
| **Kadastrinis Nr.** | 7910/0001:0431 |
| **Adresas** | Elektrėnų sav., Elektrėnų sen., **Ausieniškių k.** |
| **Plotas** | **1.6750 ha** |
| **Paskirties tipas** | 610 (žemės ūkio) |
| **Suformuotas** | 2008-05-07 |
| **Apsaugos zona** | Magistralinių dujotiekių apsaugos zona (Ambergrid) |

> ⚠️ Ankstesni dokai vadino kaimą "Kakliniškės" — KLAIDINGA. RC atvirų duomenų ir geoportal žemėlapio patvirtinta: sklypas **Ausieniškių k.**, kadastro bloke 7910/0001.

### Tikslios koordinatės (LKS94 / EPSG:3346)

- **Centroid:** `543874, 6073258`
- **Bbox:** `543753, 6073004 → 543910, 6073352` (~157 m × ~348 m)
- **Forma:** ilga siaura juosta (senas žemės ūkio rėžis), 9 viršūnių poligonas
- **Pilna geometrija:** [parcels_42/plot_7910_0001_0431.json](parcels_42/plot_7910_0001_0431.json)

### Apsaugos zonos kontekstas

Sklypas patenka į **Ambergrid magistralinių dujotiekių ir susijusios infrastruktūros apsaugos zoną** (3 lentelė, eil. Nr. 164). Prieš bet kokius darbus sklype — būtinas Ambergrid sutikimas.

### Žemėlapiai (išsaugoti projekto failuose)

| Failas | Aprašas |
|--------|---------|
| [nuotraukos/plot-highlight.png](nuotraukos/plot-highlight.png) | Sklypas pažymėtas (mėlynas outline + raudonas fill) ant NTR žemėlapio |
| [nuotraukos/plot-ntr-exact.png](nuotraukos/plot-ntr-exact.png) | Švarus NTR sklypų ribų žemėlapis (Geoportal RC kadastro) |

### Žemėlapių šaltiniai (API)

- **NTR sklypų ribos:** `https://www.geoportal.lt/mapproxy/rest/services/rc_kadastro_zemelapis/MapServer/export` (viešas, be autentifikacijos)
  - Naudotas bbox (export): `543574, 6072958, 544174, 6073558` (600 m langas), `layers=show:31,32,33`, `size=2048,2048`, `bboxSR=3346`
- **Ortofoto:** `https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/export` (ESRI, viešas)

### Vektorinių ribų šaltinis (data.gov.lt — viešas, be auth) ⭐

- **RC kadastriniai žemės sklypai (erdviniai duomenys):** https://data.gov.lt/datasets/2831/
  - Elektrėnų sav. failas: `https://www.registrucentras.lt/aduomenys/?byla=gis_pub_parcels_42.zip`
  - Formatas: GeoJSON (EPSG:3346), CC BY 4.0, atnaujinama kas mėnesį
  - 24 123 sklypai sav. teritorijoje; filtruoti pagal `kadastro_nr` lauką
  - Duomenų versija šiame projekte: 2026-06-01

### Dokumentų šaltiniai

- [Ambergrid — magistralinių dujotiekių apsaugos zonų planas](https://ambergrid.lt/lt/doclib/s37a0lrgkyef2azztx9szydwusz98v29)
- [Registrų centras — NTR paieška](https://www.registrucentras.lt/ntr/p/)
- [Regia.lt — žemės naudojimo sąlygos](https://www.regia.lt)
- [Geoportal.lt — žemėlapis](https://www.geoportal.lt/map/)
