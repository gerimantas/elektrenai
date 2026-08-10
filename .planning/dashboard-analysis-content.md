# Dashboard 1 — Turinio specifikacija

Referensas: 7910/0001:0431, centroid `54.793655, 24.682243`
Surinkta: 2026-06-17 · **Duomenys atnaujinti: 2026-08-10**

> ⚠️ **PRIEŠ IMPLEMENTUOJANT perskaityk skyrių „ATNAUJINIMAS 2026-08-10" dokumento gale.**
> Keli žemiau esantys skaičiai ir teiginiai pasenę: Rimi plotas (31k→42k m²) ir statusas
> (stato→baigta), agri kainų medianos (−18%), klasterio dinamika (neaugo), 0005 statusas
> (vis dar nespręstas). Naudok atnaujintus skaičius, ne originalius.

---

## TAB 1: FAKTAI — kas egzistuoja

### Šeimos sklypai (žemėlapyje — geltona)

| Kadastras | Savininkas | Plotas | Pastaba |
|---|---|---|---|
| 7910/0001:0428 | Virginija | 3.0501 ha | Kaimynas — ne bloke |
| 7910/0001:0429 | Audra | 1.6750 ha | Blokas |
| 7910/0001:0430 | Viktorija | 1.6750 ha | Blokas |
| 7910/0001:0431 | Aušra ir Gr | 1.6750 ha | Blokas |

**Apjungtas blokas 0429+0430+0431: 5.0250 ha**
- Riba su keliu 4728: **51.9 m** (tinka sunkvežimių įvažai)
- Laisva statybai: **3.2793 ha (65.3%)**; su KPD pritarimu: **3.8144 ha**

### Rimi logistikos centras (žemėlapyje — žalia)

| Laukas | Duomenys |
|---|---|
| Kadastras | 7910/0001:0922 |
| Plotas | 12.8495 ha |
| Suformuota | 2025-11-26 |
| Atstumas nuo bloko | ~0.5 km |
| Investicija | 60 mln. € |
| Pastatas | 31 000 m² |
| Darbo vietos | ~800 |
| Investuotojas | Darnu Group |
| Šaltinis | [Delfi 2025](https://www.delfi.lt/verslas/nekilnojamas-turtas/salia-elektrenu-pradedamos-60-mln-euru-vertes-statybos-sukurs-800-darbo-vietu-120066157) |

### AZ zonos (toggle — raudona/gintarinė)

| Zona | Plotas | Apribojimas |
|---|---|---|
| Magistraliniai dujotiekiai (Ambergrid, 25m) | 1.0973 ha | Statybų draudimas |
| Kelias 4728 AZ (20m) | 0.1133 ha | Statybų draudimas (įvaža legali) |
| Paveldosaugos AZ 119 | 0.8804 ha | KPD derinimas (ne draudimas) |
| **Griežtas draudimas iš viso** | **1.2106 ha (24.1%)** | |
| **Laisva (be apribojimų)** | **3.2793 ha (65.3%)** | |

Šaltinis: RC SŽNS raster + identify, statutory norms (SŽNS įst. 19 str.)

---

## TAB 2: TYRIMAS — signalai

### A. Paskirties keitimo prašymai (žemėlapyje — markers)

#### 🔴 Kritiniai — mūsų blokas ir tiesioginis kaimas

| Reg. Nr. | Data | Kadastras | Vieta | Keitimas | Statusas | Dok. |
|---|---|---|---|---|---|---|
| **01.3-192** | 2026-05-27 | **7910/0001:5** | Sabališkių k. (~443 m SW) | Agri → **Pramonė/sandėliavimas** | Prašymas pateiktas, **sprendimas nepaskelbtas** (tikrinta 2026-06-17) | [jpg](https://planuojustatau.lt/sites/default/files/01.3-192.jpg) |
| **01.3-151** | 2026-04-29 | 7910/0007:619+571 | **Ausieniškių k.** | Agri → Gyvenamoji | Pateiktas | [jpg](https://planuojustatau.lt/sites/default/files/01.3-151.jpg) |
| **01.3-170** | 2026-05-11 | 7910/0008:37 | **Ausieniškių k.** | Agri → Gyvenamoji | Pateiktas | [jpg](https://planuojustatau.lt/sites/default/files/01.3-170.jpg) |

#### 🟡 Kontekstiniai — Elektrėnų-Vievio koridorius

| Reg. Nr. | Data | Kadastras | Vieta | Keitimas | Dok. |
|---|---|---|---|---|---|
| 01.3-106 | 2026-04-13 | 7910/0004:230 | Vidugirių k., Vievio sen. | Agri → **Pramonė/sandėliavimas** | [jpg](https://planuojustatau.lt/sites/default/files/01.3-106.jpg) |
| 01.3-183 | 2026-05-21 | 7914/0001:152 | Lazdėjų k. | Pramonė → Komercinė | [jpg](https://planuojustatau.lt/sites/default/files/01.3-183.jpg) |

#### Statistika (Elektrėnų sav., 2026 balandis–birželis)

- Iš viso prašymų: **16**
- Iš žemės ūkio: **14 (87.5%)**
- Į pramonės/sandėliavimo: **2** (01.3-106, 01.3-192)
- Elektrėnų sen. klasteris (Ausieniškių k. apylinkė, 01.3-151 + 01.3-170): **2 prašymai vienu metu**
- Mūsų blokas 7910/0001: **1 prašymas** (01.3-192)

> Šaltinis: [tpdris.planuojustatau.lt](https://tpdris.planuojustatau.lt/) → Viešinamų TPD paieška → Elektrėnų sav.
> Lokalūs vaizdai: `.firecrawl/elektrenu-docs/`

---

### B. Pardavimo skelbimai apylinkėje (žemėlapyje — markers)

> ⚠️ **SVARBU:** Aruodas slug "ausieniskiu-k" yra **Ausieniškės (Vievio sen.)** — ~7 km nuo mūsų bloko, prie A1.
> Mūsų blokas (0428–0431) pagal RC ZIP: **Elektrėnų sen.** Kaimas pagal Google reverse geocode: **Kakliniškės**.
> Patvirtinta: Google Geocoding API + RC ZIP cross-check (2026-06-17).

#### Tiesioginė apylinkė (0–3 km) — geocoded

| Vieta | Paskirtis | Plotas | Kaina | €/ha | Koordinatės (WGS84) | Atstumas |
|---|---|---|---|---|---|---|
| Sabališkių k. | Žemės ūkio | 0.16 ha | 14 000 € | 87 500 | ⚠️ nežinomos | [elektrenuvaldos.lt](https://www.elektrenuvaldos.lt/sklypai/parduodamas-16-aru-zemes-sklypas-sabaliskese) |
| Žebertoniai, Girios g. | Agri | 2.1 ha | 24 000 € | 11 429 | `54.801476, 24.706391` | 1.78 km |
| Abromiškiai | Agri | 1.1 ha | 29 900 € | 27 182 | `54.780597, 24.716731` | 2.65 km |

#### Tolimesnė zona (5–8 km) — geocoded

| Vieta | Paskirtis | Plotas | Kaina | €/ha | Koordinatės (WGS84) | Atstumas |
|---|---|---|---|---|---|---|
| Geiboniai | Nenustatyta | 10.3 ha | 120 000 € | 11 650 | `54.752553, 24.700093` | 4.72 km |
| Pakalniškiai, Mokyklos g. | Agri+gyv. | 3.2 ha | 42 000 € | 13 125 | `54.753457, 24.758108` | 6.62 km |
| Bauboniai, Naujoji g. | Agri | 3.4 ha | 20 000 € | **5 882** | `54.765393, 24.774058` ⚠️ | 6.69 km |

#### Ausieniškės (Vievio sen.) — ~7 km, prie A1 — atskiras rajonas

| Vieta | Paskirtis | Plotas | Kaina | €/ha | Koordinatės (WGS84) | Šaltinis |
|---|---|---|---|---|---|---|
| Gėlių g. | Pramonė/sandėliavimas | 3.00 ha | 390 000 € | **130 000** | `54.781154, 24.794699` ✅ | [kampas 1047812](https://www.kampas.lt/skelbimai/sklypas-elektrenuose-ausieniskiu-k-geliu-g-parduodamas-3-ha-pramones-ir-1047812) |
| Gėlių g. 34A | Sandėliavimas (jau pakeista) | 1.03 ha | 65 000 € | **63 400** | ~`54.781, 24.795` ⚠️ | [alio ID68730617](https://www.alio.lt/skelbimai/id68730617) |
| Pramonės g. | Pramonė/sandėl./komercinė | 2.70 ha | 270 000 € | **99 300** | `54.783596, 24.782195` ⚠️APPROX | [aruodas](https://m.en.aruodas.lt/sklypai/elektrenuose/ausieniskiu-k/) |
| (be gatvės) | Komercinė | 0.744 ha | 44 000 € (+47.2%) | 59 100 | APPROX | [aruodas](https://m.en.aruodas.lt/sklypai/elektrenuose/ausieniskiu-k/) |
| Paukštyno g. | Namų valda | 0.25 ha | 22 000 € | 88 000 | `54.788177, 24.776387` ✅ | [aruodas](https://m.en.aruodas.lt/sklypai/elektrenuose/ausieniskiu-k/) — kabo 15+ mėn. |
| Aliosos g. | Namų valda | 0.239 ha | 18 000 € | 75 300 | ❌ klaidingas geocodas | [aruodas](https://m.en.aruodas.lt/sklypai/elektrenuose/ausieniskiu-k/) |

#### 2–8 km — geocoded (market_geo.json)

| Vieta | Paskirtis | Plotas | Kaina | €/ha | Koordinatės (WGS84) | Atstumas |
|---|---|---|---|---|---|---|
| Žebertoniai, Girios g. | Agri | 2.1 ha | 24 000 € | 11 429 | `54.801476, 24.706391` | 1.78 km |
| Abromiškiai | Agri | 1.1 ha | 29 900 € | 27 182 | `54.780597, 24.716731` | 2.65 km |
| Geiboniai | Nenustatyta | 10.3 ha | 120 000 € | 11 650 | `54.752553, 24.700093` | 4.72 km |
| Pakalniškiai, Mokyklos g. | Agri+gyv. | 3.2 ha | 42 000 € | 13 125 | `54.753457, 24.758108` | 6.62 km |
| Bauboniai, Naujoji g. | Agri | 3.4 ha | 20 000 € | **5 882** | `54.765393, 24.774058` ⚠️ | 6.69 km |
| Kakliniškės, Žilvičių g. | Pramonė | 0.48 ha | 95 000 € | **197 917** | `54.765393, 24.774058` ⚠️ | 6.69 km |
| Kakliniškės, šalia A1 | Agri | 3.05 ha | 299 000 € | **98 033** | ⚠️ village-level | ~7 km |

> Šaltinis: `.firecrawl/market_geo.json` (45 unikalūs, Google geocoded). Pilnas skenas: `.firecrawl/market_elektrenuose_2026-06-17.json` (119 unikalūs).

---

### C. BPD planavimo kontekstas

| Faktas | Šaltinis | Svoris |
|---|---|---|
| Kelias 4728 = **C2 miesto jungties gatvė** (ne kaimo kelias) | BPD SS-070-BPL susisiekimo brėžinys | Stiprus |
| Elektrėnai–Vievis = **1A metropolinė ašis** (aukščiausia urbanizacijos kategorija) | BPD SS-070-BPL tekstinė dalis | Stiprus |
| Ausieniškės įtrauktos į **BPD autobusų infrastruktūros planą** (maršrutas Nr.3/209) | BPD SS-070-BPL | Vidutinis |
| BPD keitimas **K-RJ-42-20-416** jau cituojamas aktyviuose DP dokumentuose | Sabališkių g. daugiabučių DP tekstas | Stiprus |

Šaltiniai:
- Tekstinė dalis: [elektrenai.lt BPD](https://elektrenai.lt/go.php/Elektrėnų%20savivaldybės%20teritorijos%20bendrasis%20planas614)
- TPDRIS: [K-RJ-42-20-416](https://tpdris.planuojustatau.lt/tpd.public.view?tpdNr=K-RJ-42-20-416)
- Lokalus failas: `.firecrawl/bpd-tekstine-dalis.pdf`

---

## TAB 3: IŠVADOS — sintetizuota analizė

### Bloko vertinimo diapazonas (5.025 ha)

| Scenarijus | €/ha | Blokas 5.025 ha | Pagrindas |
|---|---|---|---|
| RC reali sandorių kaina (zona 8.16) | 6 200 | **~31 200 €** | RC masvert sav=1191, tikri sandoriai |
| Rinkos asking mediana (3–8 ha analogai) | 8 600 | **~43 200 €** | 9 analogų iš 119 skelbimų, mediana |
| Pramonė RC reali (~350 €/a) | ~35 000 | **~176 000 €** | RC modeliuota, sandorių zonoje dar nėra |
| Pramonė asking (Ausieniškės precedentai) | 63 000–130 000 | **~316 000–653 000 €** | Aktyvūs skelbimai, ne įvykę sandoriai |

> **RC masvert šaltinis:** [registrucentras.lt/masvert](https://www.registrucentras.lt/ntr/vertinimas/masinis/masvert.php) (sav=1191, ver=36, nemokamas)
> **Rinkos skelbimai:** [aruodas.lt](https://m.en.aruodas.lt/sklypai/elektrenuose/) · [kampas.lt](https://www.kampas.lt/sklypai?city=elektrenu-sav) · [alio.lt](https://www.alio.lt/skelbimai-kategorija/id-1473/zeme/elektrenu-sav/)

### Industrializacijos signalai (faktai, ne prognozės)

1. **Rimi logistikos centras** — 12.85 ha, 60M€, 800 d.v., 0.5 km nuo bloko. Suformuotas 2025-11-26. Darnu Group. [[Delfi]](https://www.delfi.lt/verslas/nekilnojamas-turtas/salia-elektrenu-pradedamos-60-mln-euru-vertes-statybos-sukurs-800-darbo-vietu-120066157)
2. **01.3-192** — mūsų bloko (7910/0001) kitas sklypas (:5) — pateiktas prašymas keisti iš agri į pramonę (2026-05-27). Sprendimas laukiamas.
3. **Elektrėnų sen. klasteris** — 2 paskirties keitimo prašymai tame pačiame kaime per 2026 balandį–gegužę: 01.3-151 (7910/0007, Elektrėnų sen.) + 01.3-170 (7910/0008, Elektrėnų sen.).
4. **BPD metropolinė ašis** — oficialus planavimo dokumentas priskiria koridorių 1A kategorijai su C2 gatvės frontažu.
5. **Pramonės skelbimai apylinkėje** — 3 aktyvūs (63–198 k€/ha) rodo lūkesčius, bet sandorių dar nėra.

### Rinkos kainų kontekstas

| Grupė | RC reali (zona 8.16) | Rinkos asking | Premija |
|---|---|---|---|
| Žemės ūkio | **6 200 €/ha** | 5 882–27 182 €/ha | ×1–4 |
| Komercinė | 596 €/a | 591 €/a (+47.2% pabrangimas) | **×1.0** — reali rinka |
| Pramonė/sandėliavimas | ~350 €/a | 630–1 300 €/a | ×2–4 |

> Komercinė 74.4 a (+47.2%) — **vienintelis skelbimas ties realia RC verte**. Rodo realų pirkėją.
> Paukštyno g. namų valda kabo **15+ mėn.** (nuo 2025-03) — rinka nepriima ×2.4 RC premijos.

### Apribojimai (žinomi faktai)

- **Ambergrid magistralinis dujotiekis** kerta bloką — bet kokie darbai reikalauja Ambergrid sutikimo
- **Paveldosaugos AZ 119** (0.88 ha NW dalyje) — statybai reikia KPD derinimo, ne absoliutus draudimas
- **Įvaža per kelio AZ** — legali pagal SŽNS įst. 19 str., reikia Via Lietuva prisijungimo sąlygų
- Pramonės paskirties keitimas: **2–4 metai**, teisinės išlaidos, Ambergrid derinimas
- RC pramonės sandorių zona 8.16 **dar nėra** — lūkesčiai asking kainose, ne tikri sandoriai

---

## Duomenų spragos (žinomos)

| Spraga | Kaip užpildyti |
|---|---|
| Aliosos g. (Vievio sen. Ausieniškės) tikslios koordinatės | Google meta į Pilypiškės — reikia individualaus skelbimo puslapio |
| 01.3-192 sprendimo rezultatas | RC open data ZIP — `pask_kodas` lauko stebėjimas kas 1-2 sav. |
| Sabališkių 16a kadastro Nr. | UAB Fevis brokeris +370 652 52244 |
| Paskirties keitimo prašymų (01.3-151, 01.3-170) koordinatės | RC ZIP filtras pagal kadastro Nr. |
| K-RJ-42-20-416 BPD keitimo eigą | [TPDRIS puslapis](https://tpdris.planuojustatau.lt/tpd.public.view?tpdNr=K-RJ-42-20-416) |

---

## Šaltinių indeksas

| Šaltinis | URL / Failas |
|---|---|
| RC masinis vertinimas | [registrucentras.lt/masvert](https://www.registrucentras.lt/ntr/vertinimas/masinis/masvert.php) (sav=1191, ver=36) |
| RC open data ZIP | [data.gov.lt #2831](https://data.gov.lt/dataset/2831) |
| TPDRIS paskirties keitimai | [tpdris.planuojustatau.lt](https://tpdris.planuojustatau.lt/) |
| BPD SS-070-BPL | [elektrenai.lt](https://elektrenai.lt/go.php/Elektrėnų%20savivaldybės%20teritorijos%20bendrasis%20planas614) · `.firecrawl/bpd-tekstine-dalis.pdf` |
| BPD keitimas K-RJ-42-20-416 | [TPDRIS](https://tpdris.planuojustatau.lt/tpd.public.view?tpdNr=K-RJ-42-20-416) |
| Aruodas skelbimai | [m.en.aruodas.lt/sklypai/elektrenuose/](https://m.en.aruodas.lt/sklypai/elektrenuose/) |
| Kampas skelbimai | [kampas.lt/sklypai?city=elektrenu-sav](https://www.kampas.lt/sklypai?city=elektrenu-sav) |
| Alio skelbimai | [alio.lt – Elektrėnų sav.](https://www.alio.lt/skelbimai-kategorija/id-1473/zeme/elektrenu-sav/) |
| Rimi/Delfi | [Delfi 2025](https://www.delfi.lt/verslas/nekilnojamas-turtas/salia-elektrenu-pradedamos-60-mln-euru-vertes-statybos-sukurs-800-darbo-vietu-120066157) |
| 01.3-192 dok. | [planuojustatau.lt/sites/default/files/01.3-192.jpg](https://planuojustatau.lt/sites/default/files/01.3-192.jpg) |
| 01.3-151 dok. | [planuojustatau.lt/sites/default/files/01.3-151.jpg](https://planuojustatau.lt/sites/default/files/01.3-151.jpg) |
| 01.3-170 dok. | [planuojustatau.lt/sites/default/files/01.3-170.jpg](https://planuojustatau.lt/sites/default/files/01.3-170.jpg) |
| 01.3-106 dok. | [planuojustatau.lt/sites/default/files/01.3-106.jpg](https://planuojustatau.lt/sites/default/files/01.3-106.jpg) |
| Geocoded skelbimai | `.firecrawl/market_geo.json` (45 unikalūs, 8 km radius) |
| Pilnas sav. skenas | `.firecrawl/market_elektrenuose_2026-06-17.json` (119 unikalūs) |
| SŽNS overlay | RC MapProxy `rc_szns/MapServer/tile` (LKS94 tiles) |

---

# ATNAUJINIMAS 2026-08-10

Duomenys perskaičiuoti praėjus 8 savaitėms. Šie skaičiai **pakeičia** atitinkamus
aukščiau. Pilna analizė: `wiki/elektrenai/rinkos-atnaujinimas-2026-08.md`.

## TAB 1 pataisos — Rimi logistikos centras

| Laukas | Buvo | Yra |
|---|---|---|
| Pastatas | 31 000 m² | **42 000 m²** |
| Statusas | Statoma, planuota vidurys 2026 | **Statybos baigtos 2026-04** (3 mėn. anksčiau) |
| Atidarymas | — | **2026 m. vasara** |
| Sertifikatas | — | BREEAM Excellent siekis |

Šaltinis: [15min 2026-04-02](https://www.15min.lt/verslas/naujiena/nt-ir-interjeras/darnu-group-baige-60-mln-euru-vertes-rimi-logistikos-centro-elektrenuose-statybas-971-2654516)

Kiti TAB 1 duomenys (sklypai, plotai, AZ zonos, RC vertė 5 880 €) — **nepakito**.
RC vertinimo data 2026-01-01, t.y. naujausias vertinimo etapas jau atspindėtas.

## TAB 2 pataisos — signalai

### Paskirties keitimo prašymai: klasteris NEAUGO

7 nauji prašymai nuo 06-17. **Nė vienas nėra arčiau 4.6 km ir nė vienas ne į pramonę.**

| Reg. Nr. | Data | Kadastras | Vieta | Keitimas | Atstumas |
|---|---|---|---|---|---|
| 01.1-1066 | 2026-07-02 | 7910/0007:757 | Lazdynai, Vievio sen. | agri → rekreacinė | 4.62 km |
| 01.3-343 | 2026-08-05 | 4936/0003:130 | N. Kietaviškių k. | agri → gyvenamoji | 6.02 km |
| 01.3-314 | 2026-07-27 | 4936/0003:651 | N. Kietaviškių k., Birutės g. 20K | agri → gyvenamoji | 6.13 km |
| 01.3-281 | 2026-07-15 | 7967/0002:360 | Semeliškių k. | agri → rekreacinė | 14.16 km |
| 01.3-249 | 2026-06-30 | 7967/0004:371 | Daugirdiškių k. | agri → gyvenamoji | 15.70 km |
| 01.3-301 | 2026-07-23 | 7914/0004:281 | Lazdėnai, Vievio sen. | agri → gyvenamoji | n/a |
| PZNPB-K6850/6851 | 2026-08-06 | 4400-3959-0420/0440 | nenurodyta | agri → gyvenamoji | nežinoma |

**0005 (01.3-192) — vis dar nespręsta.** RC ZIP 2026-08-10: `pask_tipas=610`,
`pask_kodas=None`. Prašymas 2026-05-27, viešinimas baigėsi 2026-06-15. 2.5 mėn. tyla.
Patvirtinta savivaldybės registre: keitimas **į pramonės/sandėliavimo**, ne gyvenamąją.

**Bazinis dažnis:** per 8 sav. visoje savivaldybėje paskirtį pakeitė **1 sklypas**
(7910/0005:0510, Vievio sen., 7.94 km). Rodyti dashboarde — tai atsvara „klasteris auga".

### Rinkos kainos — visos kryptys žemyn

| Segmentas | 06-17 mediana | 08-10 mediana | Pokytis |
|---|---|---|---|
| Visa žemė | 59 140 €/ha | 48 846 €/ha | −17.4% |
| Agri ≥1 ha | 15 034 €/ha | 13 684 €/ha | −9.0% |
| **Agri 3–8 ha (mūsų analogai)** | **7 268 €/ha** | **5 952 €/ha** | **−18.1%** |
| Apylinkės zona (13 kaimų) | 34 046 €/ha | 18 652 €/ha | −45.2% |

**Pardavėjai nuleidžia, o ne parduoda:** 84 skelbimai abiejuose skenuose →
14 nuleido kainą (mediana −15.3%, giliausias −33.3%), 6 pakėlė, 64 nepakeitė.

### Agri 3–8 ha, 2026-08-10 (žemėlapio markeriai)

| Vieta | Plotas | Kaina | €/ha |
|---|---|---|---|
| Kalno g. | 3.1 ha | 8 500 € | 2 742 |
| Mustenių k. | 4.8 ha | 24 000 € | 5 000 |
| Naujoji g. | 3.4 ha | 19 000 € | 5 588 |
| Kloninių Jagėlonių k. | 3.2 ha | 18 880 € | 5 900 |
| Jarmališkių k. | 4.2 ha | 25 000 € | 5 952 |
| Pastrėvio k. | 4.4 ha | 38 000 € | 8 636 |
| Beržų g. | 3.5 ha | 59 000 € | 16 857 |
| Ežero g. | 4.8 ha | 85 000 € | 17 708 |
| **Kakliniškių k.** | **3.1 ha** | **299 000 €** | **96 452** |

**Kakliniškių 3.1 ha** — mūsų kaimo skelbimas, kaba nepakitusia kaina nuo birželio.
Dashboarde rodyti su abiem interpretacijomis: (a) lubų signalas, (b) neparduodamas
askingas. Neteikti kaip rinkos vertės — sandorio už jo nėra.

### BPD K-RJ-42-20-416

Etapai: 2022-12-16 → 2024-07-16 → 2024-11-25 → 2025-07-14 → 2025-12-04 →
**2026-03-17 (paskutinis)**. Nuo kovo nejuda. 6 metai derinime — dashboarde
pateikti kaip „ne artimiausio laikotarpio veiksnys".

## TAB 3 pataisos — išvados

Vertinimo diapazono lentelė perskaičiuojama:

| Scenarijus | €/ha | Blokas 5.025 ha | Pastaba |
|---|---|---|---|
| RC fiskalinė | 3 510 | ~17 600 € | grindys, nepakito |
| RC reali agri (zona 8.16) | 6 200 | ~31 200 € | nepakito |
| **Rinkos asking mediana (3–8 ha)** | **5 952** | **~29 900 €** | buvo 7 268 (−18.1%) |
| Pirkėjo pasiūlymas | 10 000 | ~50 250 € | dabar 1.68× virš analogų (buvo 1.38×) |
| Pramonė RC modeliuota | ~35 000 | ~176 000 € | sandorių zonoje nėra |
| Pramonė asking (precedentai) | 63 000–130 000 | ~316 000–653 000 € | asking, ne sandoriai |

**Rėminimas šeimai:** rinkai krentant, 10 000 €/ha pasiūlymo santykinė padėtis
**pagerėjo**. Birželio kontrsiūlymo intervalas (16–18k / 22–25k su 0005) buvo išvestas
iš birželio kainų ir iš prielaidos, kad 0005 netrukus išspręs. Nė viena sąlyga negalioja
— intervalą perskaičiuoti, ne perkelti.

### Signalų svoriai (peržiūrėti)

| Signalas | Buvo | Yra |
|---|---|---|
| Rimi | Stiprus (statoma) | **Stipriausias — pastatytas, patikrinamas faktas** |
| 0005 keitimas | Stiprus (sprendimas artėja) | **Silpnas — 2.5 mėn. tyla** |
| Elektrėnų sen. klasteris | Stiprus (auga) | **Silpnas — 0 naujų per 8 sav.** |
| BPD metropolinė ašis | Stiprus | Vidutinis — 6 m. derinime, nejuda |
| Rinkos trendas | Neutralus | **Neigiamas — −9…−45%, 14 nuleidimų** |

## Metodinė pastaba implementacijai

Prašymų numeracija nuo 2026-08-06 pasikeitė į **`PZNPB-K####`** (`01.3-NNN` baigėsi
ties 343). Jei dashboard turės auto-refresh, jis privalo skreipinti
https://elektrenai.lt/go.php/Prasymai962959 — `.jpg` URL zondavimas nebeveikia.

## Duomenų failai

- `.firecrawl/market_elektrenuose_2026-08-10.json` — 134 skelbimai
- `.firecrawl/parcel_diff_2026-08-10.json` — RC ZIP diff
- `.firecrawl/new_requests_2026-08-10.json` — geolokuoti nauji prašymai
- `.firecrawl/docs-new/*.jpg` — 5 nauji prašymų dokumentai
