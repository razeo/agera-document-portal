# [[aml-pravilnik]] - procedurale detalje Zakona o sprečavanju pranja novca

**Kategorija:** process / legislation (podela metodologije)
**Izvor:** Zakon o sprečavanju pranja novca i finansiranja terorizma, članovi 11–127
**Povezan sa:** [[aml]], [[kyc]], [[prijava-sumnjivih-transakcija]], [[evidencija-ovlascenih-lica]], [[doo]]

---

## 📋 Šta je ovo?

Ova stranica sadrži **procedurale detalje** iz Zakona — konkretne korake, forme, rokove i obaveze obveznika (kao što je AGERA) za sprovođenje AML sistema. Ovo je "praktični vodič" za internu implementaciju.

---

## 🔄 Tri faze AML procesa (prema Zakona)

1. **Faza 1 — Analiza rizika** (član 12–15)
   - Izrada internog akta o analizi rizika (60 dana od osnivanja/položenja djelatnosti)
   - Godišnje ažuriranje
   - Srazmerno veličini obveznika i prirodi poslovanja

2. **Faza 2 — Mjere poznavanja i praćenja** (član 17–58)
   - Identifikacija klijenta (KYC) → stvarni vlasnici → PEP
   - Praćenje transakcija (kontinuitet) → kontrola sumnjivih transakcija
   - Produbljene mjere za viši rizik

3. **Faza 3 — Dostava i evidentiranje** (član 66–127)
   - STR (sumnjiva transakcija) → FIU (≤3 dana)
   - Vođenje evidencija (min 5 godina)
   - Unutrašnja revizija

---

## 📝 Proceduralni checklist (obavezni koraci za AGERA)

### A. Pri uspostavljanju poslovnog odnosa s klijentom

| Korak | Opis | Rok / učestalost | Član |
|-------|------|------------------|------|
| **1. Identifikacija klijenta** | Pribavi: za pravno lice — naziv, sjedište, matični broj, registar; za fizičko lice — ime, JMBG, adresa, državljanstvo, lična isprava (fotokopija) | Neposredno, pre uspostavljanja odnosa | 22–26 |
| **2. Identifikacija stvarnog vlasnika (beneficial owner)** | Utvrđivanje vlasničke strukture: ispravom/memorandom o udjelima, direktima; fotokopija lične isprave stvarnog vlasnika | Neophodno za sve klijente | 42–44 |
| **3. Video-elektronska identifikacija** (opciono) | Ako se koristi, snimak video-audio zapisa, odobrenje FIU za elektronski način | — | 24b |
| **4. Utvrđivanje svrhe poslovnog odnosa** | Dokument: ugovor, nalog, pisana izjava o svrsi (knjigovodstvo, osnivanje firme, poresko savjetovanje) | — | 117/3 |
| **5. Analiza rizika klijenta** | Unos u evidenciju: faktori rizika (država, djelatnost, iznos, ponavljanje) | — | 12, 18 |

### B. Tokom poslovnog odnosa (kontinuitet)

| Korak | Opis | Učestalost / rok | Član |
|-------|------|------------------|------|
| **Praćenje transakcija** | Upoređivanje transakcija sa uobičajenim profilom klijenta; kontrola izvora sredstava | Za klijente nižeg rizika: do 2 godine između kontrola<br>Za klijente višeg rizika: do 6 meseci | 49/7 (72a) |
| **Kontrola transakcija** | Provjera indikatora sumnjivih transakcija (lista internih indikatora iz člana 83) | Na svakoj transakciji (≥15k EUR) | 66 |
| **Ažuriranje podataka klijenta** | Provera tačnosti podataka o klijentu, stvarnom vlasniku | Minimalno jednom godišnje | 43/5 (provera godišnje) |
| **Prijava FIU (STR)** | Dostava podataka o sumnjivim transakcijama | **≤3 radna dana** od saznanja za sumnju / izvršenja transakcije | 66/10, 66/6 |

### C. Po prestanku poslovnog odnosa

| Korak | Opis | Rok | Član |
|-------|------|-----|------|
| **Završna evidencija** | Evidencija sa svim podacima o klijentu (identifikacija, transakcije, dostave FIU) | — | 116 |
| **Čuvanje dokumentacije** | Čuvaj sve dokumente u skladištu (fizički/elektronski) | **5 godina** od prestanka odnosa / izvršenja transakcije | 127 |
| **Zahtev FIU za produženje** | FIU može zahtjevati duže čuvanje | Po potrebi | 127 |

---

## 📋 Evidencije koje mora voditi obveznik (član 116)

Evidencije se vode na način koji omogućava **rekonstrukciju pojedinačnih transakcija** (iznos, valuta, datum, protivstrana).

| Broj | Evidencija | Sadržaj | Čuvaj |
|------|------------|----------|-------|
| 1 | **Evidencija poznavanja i praćenja klijenta** | Identifikacioni podaci klijenta, stvarnog vlasnika, svrha odnosa, transakcije, kontrole | 5 godina |
| 2 | **Evidencija složenih i neuobičajenih transakcija** | Analiza transakcija iz člana 58 (složene/neuobičajene) | 5 godina |
| 3 | **Evidencija dostava FIU** | Podaci dostavljeni FIU (STR), datum, sadržaj | 5 godina |
| 4 | **Evidencija privremenog obustavljanja transakcija/zabrane pristupa sefu** | Naredbe FIU (član 93) | 5 godina |
| 5 | **Evidencija zahtjeva za praćenje** | Zahtjevi nadzornih organa | 5 godina |
| 6 | **Evidencija pristupa nadzornih organa** | Podaci dostavljeni nadzornim organima | 5 godina |
| 7 | **Evidencija obuke zaposlenih** | Programi, listesa, sertifikati | 4 godine od prestanka licence/obuke |

---

## 🛡️ Interni akti koji moraju postojati

| Interni akt | Svrša | Minimalni zahtevi | Član |
|-------------|-------|-----------------|------|
| **Politike, kontrole i procedure** | Glavni dokument AML sistema — obuhvata sve obaveze Zakona | Moraju biti srazmerne obimu i prirodi djelatnosti | 14 |
| **Analiza rizika** | Identifikacija i procjena rizika po klijentu, usluzi, transakciji | Pisana i elektronska forma; min. 1x godišnje ažuriranje | 12 |
| **Lista indikatora sumnjivih transakcija** | Interna lista za prepoznavanje sumnje (primeri: velike gotovinske transakcije, kompleksne strukture) | Obavezna za sve obveznike; kreira se na osnovu smjernica | 83 |
| **Procedura za KYC** | Koraci identifikacije, verifikacije, praćenja | Uključuje postupak za video-identifikaciju (ako se koristi) | 17, 24, 25 |
| **Procedura za STR** | Kako, kada i kome dostaviti sumnjivu transakciju | 3 dana od saznanja; obrazac/elektronski sistem | 66, 90 |
| **Procedura za zaštitu podataka** | Kako se čuvaju i zaštitavaju podaci klijenta | Usaglašenost sa Zakonom o zaštiti podataka | 123, 126 |

**Odgovornost za donošenje akta:** Organ upravljanja ili viši rukovodilac (član 14 stav 6). Moraju biti **odobreni i čitani od strane ovlašćenog lica** za AML.

---

## 👤 Ovlašćeno lice za AML — procedure

| Korak | Opis | Rok | Član |
|-------|------|-----|------|
| **Imenovanje** | Organ upravljanja / viši rukovodilac dodeljuje ovlašćeno lice na rukovodećoj poziciji | 60 dana od osnivanja / početka djelatnosti (ukupno) | 69 |
| **Licenca** | Ovlašćeno lice mora imati licencu iz FIU | **12 meseci** od stupanja na snagu propisa | 72 |
| **Zamjenik** | Dužno je imenovati **najmanje jednog zamjenika** | Istovremeno sa imenovanjem | 69 |
| **Dužnosti** | Koordinacija AML sistema, nadzor nad evidencijama, prijave FIU, redovno obaveštavanje organa upravljanja | Kontinuirano | 11, 14 |
| **Obuka** | Redovno stručno osposobljavanje i usavršavanje (program do Q1) | Minimalno 40 časova godišnje (prema smjernicama) | 78 |
| **Zaštita** | Obveznik mora zaštititi ovlašćeno lice od prijetnji, diskriminacije | — | 125 |

---

## ⏱️ Kritični rokovi (pregled)

| Aktivnost | Rok | Član |
|-----------|-----|------|
| **Analiza rizika (prva izrada)** | 60 dana od osnivanja / početka djelatnosti | 12 |
| **Određivanje ovlašćenog lica** | 60 dana od osnivanja (uključeno u analizu rizika) | 69 |
| **Dostava analize rizika nadzornom organu** | 3 dana od prijema zahtjeva | 12/8 |
| **Dostava STR (sumnjiva transakcija) FIU** | **≤3 radna dana** od izvršenja transakcije / saznanja za sumnju | 66/10 |
| **Dostava podataka pri prenosu novca (npr. CBC)** | Pre izvršenja transakcije (član 95) — izuzetno: odmah | 95 |
| **Godišnje ažuriranje analize rizika** | Najmanje jednom godišnje | 12 |
| **Čuvanje evidencija / dokumentacije** | **5 godina** od prestanka poslovnog odnosa / transakcije | 127 |
| **Čuvanje evidencija o obuci zaposlenih** | 4 godine od prestanka licence/obuke | 127/4 |
| **Imenovanje zamjenika za ovlašćeno lice** | Isto vreme kao imenovanje glavnog | 69 |
| **Pribavljanje licence za ovlašćeno lice** | **12 meseci** od stupanja na snagu propisa | 72 |
| **Usklađenje poslovanja sa novim zakonom** | **6 meseci** od stupanja na snagu podzakonskih akata | 143 |

---

## 📊 Indikatori sumnjivih transakcija (član 82–83 — preporuke)

Federalni zakon navodi da obveznik **sopstvenom listom indikatora** mora prilagoditi svojoj delatnosti. Primarni indikatori:

- **Visoke gotovinske transakcije** (preko 10k EUR jednokratno / kumulativno)
- **Transakcije sa lice iz visoko-rizične treće države**
- **Kompleksne pravne strukture** (trast, holding kompanije, više nivoa vlasništva)
- **Transakcije bez očigledne ekonomske opravdanosti** (član 58)
- **Ponavljanje transakcija koje odstupaju od profil klijenta** (član 49)
- **Kriptoimovina transakcije** bez jasnog porijekla

**AGERA specifični indikatori:**
- Klijent iz sektora **hotela, trgovine, usluga** — visoki gotovinski tokovi
- Klijent iz **koje se vrše česte uplate na lične račune direktora** (prenosi među povezanim licima)
- Osnivanje firmi sa **stranim kapitalom >25%** — zahtijeva dodatnu dokumentaciju

---

## 🏛️ Nadzorni organi i njihove obaveze

| Organ | Nadležnost nad | Kontakt (opciono) | Obaveze organa |
|-------|---------------|------------------|---------------|
| **Finansijsko-obavještajna jedinica (FIU)** | Svi obveznici | fiu.gov.me | Dostava STR, zahtevi za info, privremene zabrane transakcija (do 72h) |
| **Ministarstvo unutrašnjih poslova (Uprava za AML)** | Obveznici koji nisu pod nadzorom CB/agencija | mup.gov.me | Nadzor, izdavanje prekršajnih naloga, ažuriranje smjernica |
| **Centralna banka Crne Gore** | Banke, platne usluge, Pošta | cbcg.me | Nadzor nad platnim i kreditnim institucijama |
| **Poreska uprava** | Registar stvarnih vlasnika | upravaprizrake.me | Upis i čuvanje registra 10 godina |

---

## 🚨 Narušenja — šta učiniti ako detektujete sumnju?

1. **Ne izvršavaj transakciju** do dalje provere (član 93 — privremeno obustavi).
2. **Odmah obavijesti FIU** putem jedinstvene kontaktne tačke (elektronski portal).
3. **Sačuvaj dokaz** o proveri — dokumenti, email, interni nalog.
4. **Ažuriraj evidenciju** o sumnji (član 116ev. 2).

---

## 🔄 Relacije sa drugim propisima

- **Zakon o računovodstvu i reviziji** — obaveza **nezavisne interne revizije** član 80 ( AGERA mora imati nezavisnu reviziju AML sistema ako zakon propisuje).
- **Zakon o privrednim društvima** — direktorske obaveze (imenovanje, odgovornost) se preklapaju.
- **Zakon o zaštiti podataka o ličnosti** — podaci iz AML moraju biti zaštićeni; ne mogu se koristiti za komercijalne svrhe (član 126).

---

## 📝 Istorija promena (ovaj dokument)

- `2026-05-04` — inicijalna generacija — proceduralni vodič (članovi 11–127)

---

*Ova metodologija praćenja pravilnika omogućava AGERI da sistematizuje sve AML zahteve u jednu kontrolnu tablu.*
