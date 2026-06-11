# DECISIONS — Elektrėnai

2026-06-11: Dashboard papildoma informacija (paskirties keitimai, rinkos kainos, 0430 įvažos analizė) dedama į atskirą "Tyrimas" tab'ą info panelėje, ne į esamą legendą. Reason: legenda jau apkrauta (sluoksniai + SŽNS), tyrimo info — kito pobūdžio turinys, tab'as leidžia plėsti neperkraunant žemėlapio. Papildomai: 0430 ribos su keliu 4728 atkarpa (16.8 m) paryškinama žemėlapyje.
2026-06-11: AZ zonos žemėlapyje atkuriamos vektoriškai (įstatyminės normos + OSM ašys + 15 m identify grid paveldo zonai), ne iš RC raster. Reason: RC blokuoja zonų vektorius (401); raster 119 piešia tik ribos liniją — pirmas bandymas skaitmenizuoti davė klaidingą 0.02 ha vietoj tikrų 0.88 ha.
2026-06-11: Spalvų schema: šeimos sklypai 0428–0431 ryški geltona, visi kiti neon žalia, 0005 mėlynas, apjungimo kontūras raudonas punktyras; ribos virš AZ sluoksnių. Reason: vartotojo pasirinkimas, AZ štrichas nebeuždengia ribų.
2026-06-11: Legendoje tik vienas naudingo ploto skaičius (3.39 ha be kelio AZ), detali aritmetika su zonų persidengimu — Tyrimas tab'e. Reason: du skirtingi skaičiai be konteksto klaidino, plotai nesisumuoja dėl 0.3453 ha persidengimo.
2026-06-11: 0005 sprendimo patikra automatizuota cloud routine (2026-06-16 09:00). Reason: viešinimas baigiasi 2026-06-15, rankinis sekimas nereikalingas.
