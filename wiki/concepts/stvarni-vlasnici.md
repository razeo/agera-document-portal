# stvarni-vlasnici - Registar stvarnih vlasnika

> **Kategorija:** concept
> **Izvor:** Zakon o sprečavanju pranja novca i finansiranja terorizma, [[pravilnik-stvarni-vlasnici]]
> **Poslednje ažuriranje:** 2026-05-14

## 📋 Sažetak
Registar stvarnih vlasnika sadrži informacije o fizičkim licima koja u krajnjem slučaju imaju kontrolu nad pravnim licem ili privrednim društvom. Obveznici (uključujući [[knjigovodstvo]]) dužni su da identifikuju stvarne vlasnice i prijave promjene.

## 🔍 Definicija

Stvarni vlasnik je fizičko lice koje:
- Drži više od 25% udjela ili akcija u društvu
- Ima pravo na više od 25% glasačkih prava
- Ima kontrolu drugim sredstvima (preko članova društva, preko ugovora)
- Kada se ne može utvrditi, stvarni vlasnik je direktor ili odgovorno lice

## 📋 Prijava stvarnih vlasnika

### Ko prijavljuje?
- [[doo]] - članovi društva
- [[akcionarsko-drustvo]] - akcionari
- [[preduzetnik]] - preduzetnik

### Rokovi
- Prijava pri osnivanju
- Prijava promjena u roku od 30 dana
- Godišnja potvrda ispravnosti podataka

## 🔗 Povezani koncepti
- [[aml]] - AML okvir
- [[zakon-o-aml]] - AML zakon
- [[centralni-registar]] - Registar privrednih subjekata
- [[irms]] - IRMS sistem evidencije
- [[registraciona-prijava]] - Registraciona prijava

## ⚠️ Kontradikcije / Nejasnoće
- [ ] Da li postoje specifični obrasci za IRMS evidenciju?
- [ ] Da li AGERA čuva evidenciju stvarnih vlasnika za klijente?

## 📚 Izvori
- raw-sources/zakon-o-aml-extracted
- [[pravilnik-stvarni-vlasnici]]

## 📝 Istorija promena
- `2026-05-14` — Inicijalna generacija


## Opšti pregled

**Registar stvarnih vlasnika** je centrarna baza podataka u Crnoj Gori koja služi za vođenje podataka o stvarnim vlasnicima pravnih lica, privrednih društava, trustova i drugih subjekata u skladu sa **Zakonom o sprečavanju pranja novca i finansiranja terorizma**. Ovaj pravilnik propisuje način unosa, ažuriranja, provjere i pristupa podacima iz Registra.

*Službeni izvor: Pravilnik o načinu unosa, ažuriranja, provjere i pristupa podacima iz registra stvarnih vlasnika ("Službeni list Crne Gore", br. 068/24 od 19.07.2024).*


## Upravljanje i administracija

Registar je pod nadležnošću **organa uprave nadležnog za naplatu poreza** (Ministarstvo finansija – Uprava za naplatu poreza). Ovaj organ:
- Uspostavlja i održava internet aplikaciju
- Upravlja korisničkim nalozima
- Pruža tehničku podršku i nadzor nad unosom podataka
- Dostavlja izvode iz Registra nadležnim organima (član 9, 12)


## Podaci koji se vode u Registru

### Podaci o subjektu (pravnom licu/društvu/trustu)
- Naziv
- Adresa/sedište
- Poreski identifikacioni broj (PIB) ili matični broj
- Datum registracije
- Datum brisanja iz CRPS-a

### Podaci o stvarnom vlasniku
- Ime i prezime
- Adresa prebivališta ili boravišta
- Datum rođenja
- Jedinstveni matični broj (za Crnogorke) ili broj, država izdavanja i vrsta lične isprave (za strane državljanine) (član 6).


## Način unosa i ažuriranja

### Lice ovlašćeno za unos

Svaki subjekt dužan je da odredi **lice ovlašćeno za unos podataka u Registar** – to može biti zaposleno lice ili zastupnik sa prebivalištem/stalnim boravkom u Crnoj Gori. Ovo lice dobija ovlašćenje na Obrascu 1 (član 4).

### Procedura unosa/ažuriranja

1. **Pristup internet aplikaciji** – preko sredstava elektronske identifikacije visokog stepena ili kvalifikovanog certifikata za elektronski potpis (član 5).
2. **Unos matičnog broja/PIB-a** – sistem automatski preuzima podatke iz:
   - CRPS (Centralni registar privrednih subjekata)
   - Registra poreskih obveznika
   - CRS (Centralni registar stanovništva)
3. **Unos dodatnih podataka** – ručni unos podataka propisanih Zakonom koji nisu preuzeti automatski (član 6).
4. **Upload skenirane dokumentacije** – ovlašćenje, lična isprava, dokumentacija za složene strukture (član 7).
5. **Provjera tačnosti** – upoređivanje podataka iz CRPS-a/CRS-a/registara sa dostavljenim dokumentima (član 8).
6. **Potvrda** – potpisivanje izjave kvalifikovanim elektronskim potpisom (Obrazac 2) (član 8).
7. **Kreiranje izvoda** – automatsko generisanje PDF izvoda i slanje obavještenja putem e-pošte (član 6).

### Složena vlasnička struktura

Ako subjekt ima složenu vlasničku strukturu (osnivač/vlasnik je pravno lice, pravni aranžman ili drugi subjekt stranog prava), dužan je da dostavi dokumentaciju iz člana 45 stav 2 al. 2 i 3 Zakona (član 7).


## Pristup podacima (KIPS – Kompjuterizovani informacioni pravni sistem)

Registar omogućava pristup preko **internet aplikacije** i **web servisa**. Postoji nekoliko kategorija korisnika:

### 1. Finansijsko-obavještajna jedinica, nadzorni i nadležni organi
- **Pristup**: svi podaci iz Registra
- **Aptivacija**: sredstva elektronske identifikacije visokog stepena ili kvalifikovani certifikat
- **Alternativa**: zahtjev organu za naplatu poreza (bez odlaganja, u formi izvoda) (član 9)

### 2. Obveznici (banke, osiguravači, fizička lica u obavezi)
- **Pristup**: samo aktivni (trenutno važeći) podaci
- **Mogućnost prijave odstupanja**: ako utvde da podaci nisu isti, mogu uneti podatke u poseban deo Registra (to ne mijenja sadržaj Registra) (član 10).

### 3. Druga pravna i fizička lica
- **Pristup**: prema članu 47 stav 4 Zakona (javno dostupni podaci)
- **Aptivacija**: sredstva elektronske identifikacije visokog stepena ili kvalifikovani certifikat (član 11).

### 4. Korisnički nalozi i web servisi

#### Otvaranje korisničkog naloga
- Podnosi se zahtjev (Obrazac 3) organu za naplatu poreza
- Prilikom podnošenja: javni ključ
- Rok za otvaranje: **8 dana** od prijema zahtjeva (član 12).

#### Web servis
- Omogućava programski pristup preko API-ja
- Rok za omogućavanje: **8 dana** od prijema zahtjeva (član 12).


## Kontrola i nadzor

Internet aplikacija ima **aplikativno rešenje za nadzor** koje vrši automatizovane kontrole (član 13):
- Kontrola podataka i dokumentacije za složene vlasničke strukture
- Kontrola da li subjekat postoji u CRPS-u/registru poreskih obveznika/CRS-u
- Kontrola višestrukog unosa od strane istog lica
- Kontrola koršćenja nekvalifikovanih certifikata
- Kontrola godišnje nepotvrđenih podataka od strane stvarnih vlasnika
- Kontrola unosa već potvrđenih podataka
- Upareivanje sa evidencijom ograničenih lica (restriktivne mjere)

Organ nadležan za naplatu poreza može **označiti podatke za provjeru** ako utvdi netačne ili sumnjive podatke (član 13).


## Zloupotreba podataka

Ako fizičko lice utvdi da su njegovi lični podaci zloupotrijebljeni i unijeti u Registar kao podaci o stvarnom vlasniku, može podnijeti **zahtjev za izmjenu podataka** organu nadležnom za naplatu poreza (član 14).


## Bezbednost i elektronski potpis

### Kvalifikovani elektronski potpis (QES)
- **Obavezan** za unošenje i potvrdu podataka (član 6, 8)
- Izdaie kvalifikovani davalac elektronske usluge povjerenja (član 3)
- Sadrži javni ključ za verifikaciju (član 3)

### Sredstva elektronske identifikacije
- Moraju imati **visok stepen sigurnosti sistema** (član 5, 9, 10, 11).

### Čuvanje audit traga
- Sve aktivnosti povlačenja i uvidа u lične podate **automatski se pohranjuju** i povezuju sa digitalnim certifikatom korisnika (član 6).
- Omogućava rekonstrukciju ko, kada i kojim podacima je pristupao (član 6).


## Obavještenje o zaštiti podataka

Internet aplikacija prikazuje uočljivo obavještenje:

> "NEOVLAŠĆENO PRIKUPLJANJE I KORIŠĆENjE LIČNIH PODATAKA JE KRIVIČNO DJELO u skladu sa članom 176 Krivičnog zakonika Crne Gore."

(član 6).


## Prestanak važenja i stupanje na snagu

- **Prestanak važenja**: Danom stupanja na snagu ovog pravilnika, prestaje da važi Pravilnik o načinu vođenja Registra stvarnih vlasnika iz 2020. ("Službeni list CG", br. 127/20) (član 15).
- **Stupanje na snagu**: Osmog dana od dana objavljivanja u "Službenom listu Crne Gore" (član 16).


## Povezane regulative i reference

- **Zakon o sprečavanju pranja novca i finansiranja terorizma** („Službeni list CG“, br. 110/23 i 65/24) – osnovni zakonski okvir (član 4).
- **Centralni registar privrednih subjekata (CRPS)** – izvor automatskih podataka o subjektima.
- **Centralni registar stanovništva (CRS)** – izvor automatskih podataka o fizičkim licima.
- **Kvalifikovani davalac elektronske usluge povjerenja** – izdavalac elektronskih certifikata.

---

**Autor:** Pravni ekspert doo, Podgorica  
**Datum:** 12. jul 2024.  
**Pravi propis:** Pravilnik o načinu unosa, ažuriranja, provjere i pristupa podacima iz registra stvarnih vlasnika, Službeni list Crne Gore, br. 068/24 od 19.07.2024.
