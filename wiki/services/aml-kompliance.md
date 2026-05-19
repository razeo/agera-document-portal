# AML Komplajens vodič za AGERA – Računovodstvena / Knjigovodska agencija

**Autor:** Hermes Agent (Nous Research)  
**Datum:** 2026-05-3  
**Pravi aplicar:** Zakon o sprečavanju pranja novca i finansiranja terorizma (Crna Gora)  
**Cilj:** Praktični koraci za primenu AML zakona u poslovanju računovodstvene agencije

---

## 1. Izazovi za AGERE

AGERA kao **knjigovodska/računovodstvena agencija** spada u kategoriju **obveznika** prema Članu 4 stav 2 tačka 13 (usluge računovodstva i revizije). Zbog toga mora implementirati **sve mjere AML-a**, uključujući:

- **KYC (Poznavanje klijenta)**
- **Identifikaciju stvarnog vlasnika**
- **Praćenje transakcija**
- **Prijavu sumnjivih transakcija FIU-u**
- **Čuvanje evidencija (minimum 5 godina)**
- **Zapovedništvo nad AML sistemom (ovlašćeno lice)**
- **Redovna obuka i interni nadzor**

---

## 2. Koraci implementacije – Plan rada (12 mjeseci)

### 2.1 Mjesec 1–2: Osnovneoblike i analiza rizika

| Korak | Detalji | Odgovorni | Rok |
|-------|---------|-----------|-----|
| **2.1** | **Uspostavi radnu grupu za AML** – imenuj menadžera, kontakt osobu, pripravite zapisnic | Upravni organ, direktor | 1 nedelja |
| **2.2** | **Izvrši procjenu rizika** – identifikuj klijente, transakcije i rizična područja. Koristi smjernice Ministarstva i Naconalnu procjenu rizika. Napravi pismeni Analizu rizika ( Zakon 12). | Radna grupa | 30 dana od osnivanja |
| **2.3** | **Odredi kategorije rizika klijenata** (niži/viši rizik) na osnovu procjene. Kategorizuj svakog klijenta. | Odgovorni za AML | 45 dana |
| **2.4** | **Izradi interni akt o analizi rizika** – pisan dokument, potpisan od strane upravljanja. Čuva se kao trajni dokument. | Odgovorni za AML | 60 dana |
| **2.5** | **Izradi Politiku AML-a** – standardne za sve klijente (protocols). | Odgovorni za AML, pravni savet | 30 dana |
| **2.6** | **Izradi Procedure za KYC (identifikacija, verifikacija, praćenje)** – operativni koraci za zaposlene | Odgovorni za AML | 60 dana |
| **2.7** | **Izradi listu Indikatora sumnjivih transakcija** – prilagodi svom poslovanju | Odgovorni za AML | 60 dana |

---

### 2.2 Mjesec 3: Identifikacija i verifikacija – Pragmatični navodi

**KYC on boarding – obaveza za svakog novog klijenta:**

| Korak | Akcija | Dokumentacija | Član Zakona |
|-------|--------|---------------|-------------|
| **1** | **Pribavi formalnu zahtjevev za uslugama** – Ugovor, ponuda, odoobrajanje, drugo | Kopija | Član 17 |
| **2** | **Identifikuj fizičko/pravno lice** – lična isprava ili evidencija iz CRPS-a | Fotokopija lične isprave / CRPS evidencija | Član 22, 26 |
| **3** | **Provjeri identitet** – uvid u ličnu ispravu **uz prisustvo** lica ili video-identifikacija ( Član 24) | Fotokopija + zapis o identifikaciji | Član 24 |
| **4** | **Ustanovi vlasništvo** – za pravna lica: pribavi podatke o stvarnom vlasniku (beneficial owner) | Fotokopija lične isprave stvarnog vlasnika + izjava o udjelu | Član 42, 44 |
| **5** | **Provjeri.status PEP-a** – pretraži u Registru politički eksponiranih lica (FIU) | Screenshot ili izvještaj iz registra | Član 54 |
| **6** | **Pribavi podatke o transakcijama** – koji tipovi transakcija će AGERA obavljati (uplate, isplate, praćenje) | Relacije o transakcijama | Član 17, 117 |
| **7** | **Procjeni rizik** – dodeli "niži" ili "viši" rizik u sistemu | Evidencija o riziku | Član 13 |
| **8** | **Evidencija** – zapis o mjerama poznavanja (identifikaciji) i nadzoru. | Elektronički zapis | Član 116 |
| **9** | **Saglasnost** – za viši rizik ili PEP – pribavi pisanu saglasnost višeg rukovodioca | Pismo od direktora/upravljanja | Član 56 |
| **10** | **Registruj u evidenciji KYC** – u bazi, foldu, sekciji KYC | Baza podataka | Član 17 |

**Elelektronički pristup:** Koristi CRS i CRPS-elektronski servis za brzu provjeru (putem FIU-a).

---

### 2.3 Mjesec 4: Određivanje ovlaštenog lica (Compliance officer)

**Obaveže se Član 69** – Obveznik mora **odrediti ovlašteno lice za sprečavanje pranja novca** (zakonsko zaduženje).

| Zahtjev | Detalj | NAPOMENA |
|---------|--------|----------|
| **Kvalifikacije** | Završeno visoko education, najmanje 3 godine iskustva u finansijama, u oblasti prava ili računovodstva, položeni stručni ispit iz AML-a | NAPOMENA: Licenca od FIU-a ( Član 72) – FIU daje licencu nakon položenog ispita i provere. |
| **Ovlasti** | Samostalan pristup direktoru, pravo da inicirala internu istragu, hoće pristup svim dokumentima | Odgovorno lice mora biti na rukovodećoj poziciji (načelnik, direktor). |
| **Zamjenik** | Odredi zamjenika koji može da vrši funkciju u odsustvu | Obavezan je. |
| **Obaveštenje FIU** | dostavi podatke o ovlaštenom licu (ime, prezime, pozicija, kontakt, licenca) | Forma FIU-a, dostava elektronski. |
| **Izrada uloge** – piše se uloga za ovlašteno lice, definišu se dužnosti, prava, odgovornost | Interni akt | Član 69 |
| **Kontakt sa FIU** – razmjena informacija, nadzor | Odgovorno lice je jedini kontakt | Član 72 |

**Sugestija za AGERA:** Menadžer/partner s licencu računovodstva može biti ovlašteno lice. Za velike agencije – zamenik menadžera.

---

### 2.4 Mjesec 5: Sistem praćenja transakcija i detekcije

**Izradi sistem praćenja:**

1. **Identifikuj transakcije koje spadaju pod obavezu prijave** – sve transakcije koje AGERA izvrši ili pomaže izvršiti:
   - Pravno: prenose sredstava između računa (bankovni nalog).
   - Kupoprodaje imovine (npr. imovina, vozila).
   - Prikupljanje sredstava za klijente.
   - Pravni poslovi (položine, osiguranja).
   - Prenos kripto-imovine (ako se pruža).

2. **Postavi proceduru za nadzor**:
   - Svaka transakcija mora imati **oznaku** – je li uspostavljena ili nije. Ako nije – mora biti uzrokovana potpisa i pravo.
   - Transakcije veće od **15.000 EUR** – posebna pažnja, evidenca, prijava ako postoji sumnja ili ako se spaja.

3. **Koristi indikatore sumnje ( Član 83) i makro-ekonomske indikatore**:
   - Lemu: `CHECK_AMOUNT_LIMIT`, `CHECK_PEP_STATUS`, `CHECK_STRUCTURE_TRANSACTIONS`, itd.

4. **Automatska blokada/suspendovanje** ( Član 93):
   - Ako FIU naredba o blokadi – postoji sistem da se **transakcija odmah zaustavi**.
   - Interno: Ako se identifikuje sumnja – preporuka za **dozvolu nadzornika** (odobrenje direktora) i **obaveštavanje klijenta**.

5. **Implementiraj proces:**
   a) Generisanje elektronicnih izveštaja o transakcijama (CSV/Excel).
   b) Ručna provjera – ako automatski ne prepozna.
   c) Dnevna pregleda: `>15.000 EUR` i `/`sumnjivi` transakcije.

---

### 2.5 Mjesec 6: Obuka zaposlenih

**Zaposleni moraju biti osposobljeni** ( Član 78) u oblasti AML-a:

| Tip obuke | Sadržaj | Učesnici | Period |
|-----------|---------|----------|--------|
| **Uvodna obuka** | Zakon, definicije, obaveze, KYC, prijave, sankcije | Zaposleni u računovodstvu, izvršavanje transakcija | Prvi mj. |
| **Stručni ispit** | Pravni ispit iz AML-a (za ovlašteno lice) | Ovlašteno lice (ophod) | Odmah |
| **Godišnja obuka** | Novine, najava amendmana, primjeri slučajeva | Svi zaposleni | Svake godine |
| **Specifične procedure** | Video identifikacija, zahtjev kod FIU-a, evidencija | Zajedno sa IT | Prvi mj. |

**Dokumentacija:** Svi prisustvuju **potvrde o obuci** – čuvaju minimum 5 godina.

---

### 2.6 Mjesec 7: Napravi evidencije ( Član 116,117)

AGERA mora voditi **elektroničke i papirnate evidencije**:

**Evidencija A: Klijenti i KYC podaci**

| Stupac | Sadržaj |
|--------|---------|
| ID klijenta | Broj, ime, naziv |
| Tip klijenta | Fizičko/pravno/trgovački poduzetnik |
| Identifikacioni podaci | JMBG/Matični broj, adresa, lična isprava |
| Stvarni vlasnik | Ime, lična isprava, odnos (25%+ udjel) |
| Status | Rezident/nerezident, PEP |
| Datum uspostave | Date of relationship |
| Vrsta posla | Računovodstvo, prijave, konsultacije |
| Rizik | Nizak/visoki (pojednostavljeni) |
| Verzija identifikacije | Fizičko prisustvo/video/ekvivalent |
| Dokumenti | Ugovor, PIB, tekući računi, bankovni računi |
| Izvještaj za savjetovanje | Analiza i skucanje |

**Evidencija B: Transakcije i poslovi ( Član 117)**

| Kolona | Podatak |
|--------|---------|
| Datum transakcije | 2025-03-15 |
| Vrsta transakcije | Uplata/Isplata, kupoprodaja |
| Iznos (EUR) | 25000 |
| Valuta | EUR |
| Svrha | Plaćanje računa za materijal/invoice #123 |
| Broj naloga | 2025-045 |
| Poslovni kod | 5000 (usluge) |
| Klijent | ABCD d.o.o. |
| Podaci o platiocu/primaocu | Banka ××, račun Ž× |
| Indikatori | Iznos > 15.000 EUR, očekivano profil |
| Sumnjiv je (DA/NE) | DA (nerazumljiva svrha) |
| Prijava FIU (DA/NE) | DA, broj prijave FIU-2025-034 |
| Uzrok | Nepravilnost, sumnjivo ponašanje |
| Radnik koji je zaprimio | Nicolaa |

**Evidencija C: Izvještaji FIU**

| ID prijave | Datum | Sadržaj (kratak opis) | Status (čekanje/odgovor/raskid) |
|------------|--------|----------------------|----------------------------------|

**Evidencija D: Interna revizija i kontrolisanje**

- Datumi revizija
- Pitanja/potencijalni nedostaci
- Istraživanja
- Zaključak

**Evidencija E: Obuka zaposlenih**

- Ime, pozicija, datum obuke, sadržaj, potvrdio predavač.

**Tehnički zahtjevi:** Baza podataka (Excel, Access ili specijalizovan softver) mora biti zaštićena, sa backupom, dostupna za nadzor.

---

### 2.7 Mjesec 8: Izrada listi indikatora ( Član 83)

Obveznik mora **sastaviti sopstvenu listu indikatora** za prepoznavanje sumnjivih klijenata i transakcija ( Član 83). Ova lista se **ažurira najmanje jednom godišnje**.

**Predlog indikatora za AGERA-a (primeri):**

1. **Transakcije iznad praga:**
   - Iznos > 15.000 EUR u gotovini.
   - Više transakcija u roku 24 časa ukupno > 15.000 EUR.
   - Prenos više od 100.000 EUR bezgotovinski (povremeni).

2. **Klijent sa sumnjivim profilom:**
   - Klijent iz visoko-riziičnih zemalja (nezadovoljan).
   - Klijent sa lošom reputacijom u javnosti.
   - Politčki eksponirano lice (PEP).
   - Klijent se ne može dobro identificirati.

3. **Poslovni odnosi:**
   - Više firmi pod istim direktoru/ovlascenicima.
   - Klijent koristi više RAČUNOVODSTVENIH agencija istovremeno.

4. **Transakcije bez očiglednog razloga:**
   - Velike transakcije ka nedavno osnovanom klijentu.
   - Velike transakcije ka nepoznatom primaocu.
   - Veliki iznosi za "usluge" koje nisu normalne za profil klijenta.

5. **Kripto imovina:**
   - Velike transakcije kripto-valute (npr. Bitcoin) iznad 1.000 EUR.
   - Više transakcija na različite novčane račune (komplicirane).

**Lista indikatora** treba da bude **dokumentovan** i dostupan svim zaposlenima.

---

### 2.8 Mjesec 9: Pregled dokumentacije i čuvanje

**Čuvanje evidentije**:

- **Minimalno 5 godina** od prestanka poslovnog odnosa (Član 127).
- Čuvanje **u originalu ili kopiji** (fizički ili elektronički).
- Privatna dokumentacija (ugovori, izjave, odobrenja, indikatori, evidencije transakcija, prijave FIU, slike i identifikacioni zapisi).

**Obaveze retencije**:
- Za **fizičko lice** – 5 godina od prestanka robne relacije.
- Za **pravno lice** – 5 godina od prestanka usluge.
- Za **transakciji** – 5 godina od izvršenja.
- Za **prijave FIU** – 5 godina od podnošenja.
- Za **obuku zaposlenih** – dokazi o obuci.

**Kako čuvati:**
- **Digitalno** – čuvati na sigurnom serveru, backup, šifrovanje.
- **Fizički** – arhiva u zaključanom prostoru.

**Zabrana uništenja** – dokaznog perioda nije dozvoljeno uništiti ništa što FIU mohte tražiti.

---

### 2.9 Mjesec 10: Nadzor i unutrašnja revizija

**Unutrašnja kontrola i revizija** ( Član 80):

- Obveznik mora **organizovati redovnu kontrolu i reviziju** sprovođenja politika i procedura.
- **Nezavisna interna revizija** – ako Zakon o računovodstvu to zahteva – obavezna je.
- **Procjena adekvatnosti, pouzdanosti i efikasnosti** sistema upravljanja rizikom.

**Plan revizije:**

| Frekvencija | Oblast | Odgovorni |
|-------------|--------|-----------|
| Kvartalno | KYC dokumentacija | Internal audit |
| Polugodišnje | Transakcije i indikatori | Compliance |
| Godišnje | Cjelokupan AML sistem | Spoljni auditor (opciono) |

**Nalazi revizije** – dokumentovani, sa preporukama i planom ispravki.

---

### 2.10 Mjesec 11–12: Integracija i priprema za nadzor

**Proveri ispravnost:**

| Stavka | Da li je spremno? |
|--------|-------------------|
| Analiza rizika dokumentovana | Da/Ne |
| Politika AML-a (pismeni akt) | Da/Ne |
| Procedure KYC dokumentovane | Da/Ne |
| Lista indikatora dostupna | Da/Ne |
| Ovlašteno lice odabrano i obavešteno FIU | Da/Ne |
| Licenca za ovlašteno lice (položeni ispit) | Da/Ne |
| Evidencije uspostavljene (elektroničke i papirnate) | Da/Ne |
| Obuka zaposlenih dokumentovana | Da/Ne |
| Unutrašnja revizija planirana | Da/Ne |
| Sistem za dostavu FIU (elektronički) | Da/Ne |
| Pristup CRS/CRPS-elektronički | Da/Ne |
| Sigurnosni protokoli i zaštita podataka | Da/Ne |

**Pripremi se za nadzor:**

- Nadzorni organi (Ministarstvo unutrašnjih poslova, FIU) mogu **izvršiti inspekciju**.
- Prate sve dokumente: analizu rizika, evidenciju, prijave, obuku.
- Isto tako **FIU može tražiti podatke** i izvršiti dodatnu proveru.
- **Zapamtite:** Nema izuzetka za AGERA (osim advokat/notar) – sve mora biti dostupno.

---

## 3. Procedura za normalno poslovanje – dnevne nedeljne tasks

### 3.1 Klična odgovornost: Odgovornost za AML – `ovlašteno lice`

- **Dnevno:** Pregled sumnjivih transakcija (iz automatskog sistema).
- **Sedmično:** Analizira transakcije > 15.000 EUR.
- **Mesečno:** Ažuriranje evidencija klijenata, provera PEP statusa, ažuriranje analize rizika.
- **Kvartalno:** Obeležavanje potencijalnih nedostataka, priprema za reviziju.
- **Godišnje:** Određivanje prijave FIU-oze za analizu rizika, ažuriranje liste indikatora, unutrašnja revizija, obnova licence ovlaštenog lica.

### 3.2 Zaposleni u računovodstvu

- **Dnevno:** Prikupljanje dokumenata od klijenata (fakture, računi), unos u sisteme.
- **Tokom prijave:** Za svaku transakciju – provjera da li postoji **KYC evidence** za klijenta.
- **Na zahtjev:** Dostaviti dokumentaciju FIU ili nadzornim organima.
- **Obeležavanje:** Ako sumnja u sumnjivost transakcije – odmah se **prijavi ovlaštenom licu**.

### 3.3 Menadžment

- Slediti **budžet za AML** (obuka, softver, licenciranje).
- **Periodično pregledati izveštaje** iz FIU-a i analizu rizika.
- **Revidirati politike** u slučaju promena u zakonu.

---

## 4. Tipovi dokumenta koje AGERA mora imati

| Dokument | Sadržaj | Kome dostaviti? |
|----------|---------|-----------------|
| **Analiza rizika** | Opis rizika po klijentima, geografiji, proizvodima | Upravni organ |
| **Politika AML** | Ciljevi, organizacija, uloge, procedure | Svi zaposleni |
| **Procedure KYC** | Koraci identifikacije, verifikacije, praćenja | Zaposleni izvođači |
| **Lista indikatora** | Indikatori sumnji za transakcije i klijente | Zaposleni, ovlašteno lice |
| **Evidencije KYC** | Tabela klijenata, podaci, dokumentacija | Ovlašteno lice, FIU |
| **Evidencije transakcija** | Detaljni podaci o transakcijama ( Član 117) | Ovlašteno lice, FIU |
| **Prijave FIU** | Kopije svih STR-a (sumnjivih transakcija) | Ovlašteno lice |
| **Dokumentacija o obuci** | Potvrde o obuci, kursevi | Ovlašteno lice, nadzorni organ |
| **Zapisi o internim revizijama** | Nalazi, preporuke | Upravni organ |
| **Pravila zaštite podataka** | Kako se čuvaju podaci, ko ima pristup | Ovlašteno lice, IT |

**Čuvanje:** Minimum 5 godina od prestanka odnosa ili obaveza ( Član 127).

---

## 5. Elektrončki identifikacioni proces ( Član 22–24)

AGERA može koristiti **video-identifikaciju** za klijente koji ne mogu biti prisutni.

**Koraci video-identifikacije ( Član 24):**

1. **Kontaktiraj klijenta** putem video-poziva (Zoom, Teams, itd.).
2. **Informiši klijenta** da će se sumnja snimati (audio+video) i da će se snimka čuvati.
3. **Povedi identifikaciju**:
   - Zahtevaj da klijent drži ličnu ispravu (npr. lična karta) prema kameri.
   - Snimi lice i dokument.
   - Pitanja za potvrdu: "Da li sam ja [ime i prezime]?".
4. **Pročitaj podatke iz lične isprave** (elektronski – ako je moguće, inače ručno).
5. **Pribavi sliku i elektronski potpis** (ako je moguće).
6. **Proveri putem FIU** (CRS, evidencija izdatih isprava, baza ukradenih).
7. **Ako je sve u redu** – snimak se čuva u evidenciji.
8. **Ako postoje nedoumice** – obustavi identifikaciju i zahtevaj fizičko prisustvo.

**Obaveze:** Morate imati **sistemsko rešenje** za prikupljanje, čuvanje i bespravljanje snimaka – sa dostupnošću za nadzor.

---

## 6. Elektronska identifikacija bez prisustva ( Član 23)

Samo ako klijent pribavlja **elektronsku ličnu ispravu** i **kvalifikovani elektronski identifikator** – moguće je izvršiti identifikaciju **bez prisustva**.

**Procedura:**

1. Klijent dostavlja **fotokopiju lične isprave** (elektroniko).
2. Pribavi **sertifikat za elektronski potpis** ili sredstvo visokog stepena sigurnosti.
3. Pročitaj podatke iz dokumenta.
4. **Provjeri elektronski** putem FIU-a (CRS, evidencija izdatih isprava, baza ukradenih).
5. Ako su podaci identični – uspostavi poslovni odnos.
6. Ako postoje razlike – **blokiraj** i obaveštaj FIU.

**Napomena:** AGERA ne može koristiti elektronsku identifikaciju za klijente iz **visoko-riziičnih** država.

---

## 7. Sumnjiva transakcija – Primjeri za AGERA-a

| Scenario | Indikatori | Da li je sumnjivo? | Da li se prijavljuje? |
|----------|------------|-------------------|-----------------------|
| Klijent šalje 20.000 EUR na račun u inostranstvu, nepoznat primaoc | Visok iznos, nepoznata svrha | Da | Da |
| Klijent traži da se sredstva podjela na više malih transakcija (structuring) | Više transakcija ispod praga | Da | Da |
| Klijent nema dokumentaciju za izvor sredstava, a transakcija je 50.000 EUR | Nedostatak dokaza | Da | Da |
| Klijent je PEP, a transakcija je 30.000 EUR na off-shore račun | Politčki eksponirano lice, visoko rizično | Da | Da |
| Klijent kupuje imovinu za gotovinu 80.000 EUR (veće od 15.000 EUR) | Gotovina, visoka vrednost | Da | Da |
| Klijen traži da se transakcija izvede putem trećeg lica (npr. brat/sestra) | Pokrivanje stvarnog vlasnika | Da | Da |
| Klijent koristi više firmi pod istim direktoru za istu uslugu | Structuring, avoiding detection | Da | Da |

---

## 8. Kontrolna lista – AML Compliance Check‑List

**Dnevno:**
- [ ] Pređi pregled transakcija za prethodni dan:
  - Ako postoji bilo koji iznos >= 15.000 EUR – markiraj za detaljan pregled.
  - Ako više transakcije ukupno > 15.000 EUR – pregledaj.
  - Ako je transakcija sumnjiva – prijavi (istočno).
- [ ] Procitaj sosjet navedene na sumnjivim transakcijama.
- [ ] Osiguraj da svi zaposleni imaju pristup indikatorima.

**Sedmično:**
- [ ] Sastanak sa ovlaštenim licem – pregled svih označenih transakcija.
- [ ] Ažuriranje listi PEP-a i visoko-rizīčnih teritorija.
- [ ] Možda proveravati evidencije za svakog klijenta koji je na višem riziku.

**Mesečno:**
- [ ] Ažuriranje analize rizika – član 12.
- [ ] Revizija KYC evidencije – potvrdi identifikaciju za sve klijente (svake godine minimum).
- [ ] Pregled obaveza pri prenosu ( Član 35) – da li svi prenosi imaju potrebne podatke.
- [ ] Proveriti da li sve transakcije imaju dokumentaciju.

**Godišnje:**
- [ ] Nova analiza procjene rizika.
- [ ] Ažuriranje liste indikatora.
- [ ] Pregled kroz unutrašnju reviziju.
- [ ] Dostavljanje izveštaja FIU ( Član 81).
- [ ] Obnova licence ovlaštenog lica ( Član 72).
- [ ] Punktuiranje obuka.
- [ ] Destroying documents older than 5 years (optional).

---

## 9. Primeri forme i dokumenta

### 9.1 KYC obrazac za novog klijenta (pravačno lice)

```
IME FIRME: ________________________
MATIČNI BROJ: ______________________
PIB: ______________________________
ADRESA SJEDIŠTA: _______________________________________
TELEFON: __________________________ E-MAIL: _______________

1. OSOBE:
   ___________________(JMBG)  ___________________ (adresa) 
   Lisicna: __________________ (broj, datum izdavanja, organ)

2. STVARNI VLASNIK (≥25%):
   Ime/Prezime: ______________________
   JMBG: ____________________________
   Udio: _____ %   Adresa: _______________________________
   Lična isprava: ___________________

3. ZASTUPNIK (Direktor):
   Ime/Prezime: _______________________
   Pozicija: __________________________
   Lična isprava: __________________

4. PEP status: [ ] DA [ ] NE

5. RIZIK KLIRIJENTA: [ ] NIŽI [ ] VIŠI

6. VRSTA POSLA: _______________________________________

7. DATUM USPOSTAVE ODNOSA: ____________________________

8. IDENTIFIKACIJA VRŠENA: [ ] Lično [ ] Video [ ] Elektronski

9. DOKUMENTI: 
   [ ] Ugovor
   [ ] Statut
   [ ] Lične isprave
   [ ] Izjava o stvarnom vlasniku

POTPIS OVLAŠĆENOG LICA: _____________________ DATUM: _______
```

### 9.2 Transakcijski evidencijski obrazac ( Član 117)

```
ID transakcije: ______________________________
DATUM: ____/____/______
VRSTA: [ ] uplata [ ] isplata [ ] presjek 
IZNOS: ______ EUR  (puna valuta)
VALUTA: _______
BROJ NALOGA: _______________________________
POSLOVNI KOD: _______________________________
SV__________ izvršio: (ime i prezime zaposlenog)

KLIRIJENT:
   Ime: ______________________________________
   Pravni status: _____________________________

PREMA:
   Ime: ______________________________________
   Vrsta: [ ] Fizičko [ ] Pravno [ ] Preduzetnik

Transakcija opširno: _________________________________
Svrha transakcije: _________________________________

INDIKATORI:
   [ ] Iznos > 15.000 EUR
   [ ] Složena struktura
   [ ] PEP
   [ ] Sumnjivo ponašanje
   [ ] Nedostatak dokumentacije

Sumnjivo? [ ] DA [ ] NE
Ako DA – prijaviti FIU: [ ] DA [ ] NE (broj prijave ________)
```

### 9.3 Prijava FIU – STR (Suspicious Transaction Report) – sadržaj ( Član 66 stav 4)

```
Podaci o obvezniku:
   Naziv: AGERA d.o.o.
   Adresa: ____________________________
   PIB: _______________________________
   Kontakt osoba: ___________________

Podaci o klijentu:
   Ime/Prezime/Naziv: _____________________
   JMBG/Mat. br.: _______________________
   Adresa: _______________________________

Identifikacija stvarnog vlasnika (ako postoji):
   Ime/Prezime: __________________________
   JMBG: _________________________________
   Udio: ______ %

Transakcija:
   Datum: ____/____/______
   Vrsta: _________________________________
   Iznos: ________ EUR (valuta)
   Svrha: _________________________________

Razlog sumnje: ___________________________
   (opis sumnjivih okolnosti)

Dokumentacija priložena:
   [ ] Kopija fakture
   [ ] Bankovni izvodi
   [ ] Ugovor
   [ ] Drugo: _____________________________

Poverljivost: Obrazloženje po Članu 84.

Potpis ovlašćenog lica (kvalifikovani sertifikat): ____________________
```

---

## 10. Elektrončki sistem za AML

**Preporuka:** Koristi specijalizovan softver za AML za mala i srednja preduzeća (npr. `ComplyAdvantage`, `Identity.com`, `LexisNexis`, `ACTICO`).

**Svojstva:**
- Automatska provjera PEP-a (globalna lista).
- Indikatori sumnji (automatsko uklanjanje limitnih transakcija).
- Elektrončke prijave FIU (povezivanje).
- Čuvanje evidencija (backup, 5+ godina).
- Audit trail – zapis svih aktivnosti.

**Alternativa (za pocetnike):**

- **Excel tabela** za evidenciju klijenata i transakcija.
- **Fajl sistem** za čuvanje dokumenata (skenirani KYC dok).
- **Rutinska provera PEP-a** preko FIU sajta (ručno).
- **Ručna prijava** preko FIU elektročnog portala (ako postoji).

**Napomena:** Kako bi se izbjeglo kažnjavanje, **elektronski sistem mora biti pouzdan i dostupan za nadzor**.

---

## 11. Oblasti koje zahtijevaju posebnu pažnju

### 11.1 Klijenti iz visoko-rizik zemalja ( Član 59)

- **Visoko-rizik teritorije** – definisane FIU (recimo: Iran, Severna Koreja, Sirija, itd. – prema EU i UN listi).
- **Za ovakve klijente:**
  - Obaveza dodatne provere izvora sredstava.
  - Pribavi pisanu saglasnost višeg rukovodioca ( Član 59).
  - Pojačano praćenje (maksimalno 6 meseci, umesto 2 godine).
  - Viša frekvencija transakcija.

### 11.2 Trgovci opreme i robom

- **Transakcije od 10.000 EUR** – obavezna prijava (pravac FIU).
- Isto za **fizičke i pravne lica** koji vrše trgovinu (češće kod klijenata AGERE – ako AGERA pomaže u trgovini robom).

### 11.3 Izdavanje faktura i prijem plaćanja

**AGERA izdaje fakture** za klijente – **obavezan** da pribavi podatke o stvarnom vlasniku:
- Ako klijent pravno lice – pribavi podatke o stvarnom vlasniku.
- Za velike iznose – eventualno tražiti dodatnu dokumentaciju.

### 11.4 Kriptoimovina ( Član 4a)

- Ako AGERA pruža usluge vezane za **kripto imovinu** – dodatan nivo kontrole.
- Transakcije >= 1.000 EUR – obavezna prijava ( Član 18 stav 1 tačka 8).
- Identifikacija Vladmira (kako se koristi saznanje – moguća samo video identifikacija ili lično).
- Za klijente iz visokorizičnih teritorija – zabranjeno.

---

## 12. Povratne informacije od FIU – Šta raditi nakon prijava

**( Član 68)**

1. **FIU šalje povratnu informaciju** – da li postoje osnovi sumnje:
   - Ako **NEMA sumnji** – obveznik nastavlja normalno poslovanje.
   - Ako **POSTOJI sumnja** – FIU preporučuje da obveznik:
     - **Raskine poslovni odnos**.
     - **Blokira od sebe** transakciju.
     - **Povraćaj sredstva**.
2. **Obveznik je dužan da postupi po preporuci** – npr. raskid odnosa.

**Primjer:** Ako FIU pošalje poruku: "Raskidite poslovni odnos sa klijentom X zbog sumnje u pranje novca" – AGERA je dužna da **prekine sve poslove sa tim klijentom** i **blokira račune** ( Član 68, Član 93).

**Evo:** FIU može narediti privremenu blokadu računa/fondova – **obveznik mora poslušati**.

---

## 13. Raskid poslovnog odnosa ( Član 68)

**Kada raskinuti:**

- Na zahtjev FIU ( Član 68).
- Kada AGERA sama identifikuje sumnju i ne može dobiti objasnjenja (npr. ne prikuplja dokumente).

**Procedure:**

1. **Obavijesti klijenta** o razlogu (ako FIU dozvoljava).
2. **Blokiraj račune** (ako je to primenjivo).
3. **Ispiši sve dokumente** u vezi sa klijentom – sačuvaj dokumentaciju za FIU.
4. **Ažuriraj evidenciju** – označi status "raskid".
5. **Dostavi obaveštenje FIU** o raskidu ( Član 66).

---

## 14. Zaštita podataka ( Član 125–126)

**Obaveza:** Podaci dobijeni iz KYC i evidencije **čitaju se u skladu sa zakonom o zaštiti podataka**.

**Što čuvati:**

- Lične isprave (fotokopije).
- Podatke o transakcijama.
- Svrhe poslovnih odnosa.
- Informacije o izvoru sredstava.

**Za koliko dugo:** Minimum 5 godina od prestanka odnosa.

**Kome otkrivati:**

- Samo **ovlaštenom licu**, zaposlenima izravno uključenim u transakcije, **FIU** i nadzornim organima ( Član 84).
- **Ne otkrivati** klijentu da ste prijavili sumnjivu transakciju (osim ako ne raskidate odnos – onda je dozvoljeno).

---

## 15. Crno-Bela lista: Ako ne postupaš ( Član 137)

**Novčana kazna** za obveznike (pravna lica):

| Prekršaj | Kažnjenje (EUR) |
|----------|-----------------|
| Neprijava sumnjive transakcije (uključujući indikatore >15k EUR) | 5.000 – 20.000 |
| Neodgovarajuća identifikacija klijenta | 5.000 – 20.000 |
| Ne vođenje evidencija (član 116) | 5.000 – 20.000 |
| Nečuvanje evidencija (član 116) | 5.000 – 20.000 |
| Ne postojanje internih akata (politika) | 5.000 – 20.000 |
| Ne postojanje ovlašćenog lica | 5.000 – 20.000 |
| Ne organizovanje obuke (član 78) | 5.000 – 20.000 |
| Ne postojanje novečke interne revizije (član 80) | 5.000 – 20.000 |
| Povjerenje trećem licu (kada je zabranjeno) | 5.000 – 20.000 |
| Kršenje tajnosti (član 84) | Do 6 mjeseci, novčana kazna |

**Fizičko lice (odgovorni):** 500 – 2.000 EUR.

**Otvorenje:** Policija i FIU pokreću prekršajni postupak.

---

## 16. Podrška od nadzornih organa

**Kontakti za AGERU (Crna Gora):**

- **Finansijsko-obavještajna jedinica (FIU):**
  - Adresa: Podgorica, [tačna adresa]
  - Web: https://fiu.gov.me
  - Telefon: +382 20 510 400

- **Ministarstvo unutrašnjih poslova** (nadzor):
  - Uprava za privredne prekršaje

- **Centralna banka Crne Gore** (ako se primjenjuje na banke):

- **Agencija za nadzor osiguranja** (ako se primjenjuje):

---

## 17. Povjerenje: "Šta ako uradim sve ovo?"

**Prednosti:**

1. **Zaštita od kazni** – izbegavanje novčanih kazni.
2. **Čuvanje reputacije** – klijenti uvere u sigurnost.
3. **Smanjenje rizika** – manje šansi da AGERA bude uključena u pranje novca.
4. **Pravna sigurnost** – ispunjava sve obaveze.

**Ako ne uspemo:**

- FIU može pokrenuti **prekršajni postupak** (odmah).
- **Novčane kazne** od 5.000 do 20.000 EUR.
- **Prekid poslovanja** (privremena zabrana rada) – od FIU.
- **Odsustvo licence** – za ovlašteno lice ( Član 72).
- **Krivicna odgovornost** (ako postoji umiješanost u pranje novca) – zatvor do 8 godina (ne ovaj zakon, već Krivični zakonik).

---

## 18. Zaključak – Pet koraka za uspeh

1. **Imati jasnu strukturu** – Obavezno imenovati ovlašteno lice.
2. **Voditi evidencije** – KYC i transakcije u digitalnom sistemu.
3. **Izvještavati sumnje** – bez obzira na iznos, Djela 66.
4. **Redovno se podizati** – obuka, revizija, ažuriranje.
5. **Čuvati sve** – dokumentaciju minimum 5 godina.

---

## 19. Tel: Članovi

| Član | Tema | Minimalna obaveza za AGERU |
|------|------|---------------------------|
| **Član 4** | Obveznici | AGERA je obveznik (računovodstva i revizija). |
| **Član 11** | Osnovne obaveze | Primijeniti sve mjere (KYC, evid, prijave, obuka). |
| **Član 12** | Analiza rizika | Izraditi analizu rizika (60 dana od osnivanja). |
| **Član 14** | Upravljanje rizikom | Izraditi politiku i procedure. |
| **Član 17** | Mjere poznavanja | Identifikacija klijenta (identitet, stvarni vlasnik, transakcije). |
| **Član 18** | Kada sprovesti mjere | Prije uspostave odnosa i izvršenja velikih transakcija (15k/10k). |
| **Član 22** | Identifikacija fizičkog lica | Uvid u ličnu ispravu + fotokopija + upis. |
| **Član 23** | Elektronska identifikacija | Moguća bez prisustva. |
| **Član 24** | Video identifikacija (žestok) | Sa jasnim uslovima. |
| **Član 26** | Identifikacija pravnog lica | Izuzev iz CRPS-a. |
| **Član 42–44** | Stvarni vlasnik | Identifikacija i evidenciranje (≥25% udio). |
| **Član 49** | Praćenje odnossa | Dovoljno informacija (max 6 mjeseci za visoki rizik, 2 godine za niski). |
| **Član 54–56a** | Politčki eksponirano lice (PEP) | Provera u registru, dodatne mjere. |
| **Član 58** | Složene transakcije | Za složene transakcije – utvrđivanje svrhe i namjere. |
| **Član 59** | Visoko-rizik države | Dodatni zahtjevi za klijente iz tih država. |
| **Član 66** | Prijava sumnjivih transakcija | Dostava bez odlaganja (pog. 2 i 3 transakcije >15k EUR). |
| **Član 67** | Izuzetak za advokate | **Nije primenjivo na AGERU.** |
| **Član 69–72** | Ovlašćeno lice | Imenovanje, obaveštenje FIU, lična licenca (ispit). |
| **Član 78** | Obuka zaposlenih | Minimalno jednom godišnje. |
| **Član 80** | Unutrašnja revizija | Redovna kontrola. |
| **Član 83** | Lista indikatora | Sastaviti sopstvenu listu indikatora (ažurirati godišnje). |
| **Član 116** | Vrste evidencija | Vodi evidenciju: Klijenti, transakcije, prijave, interni nadzor, obuka. |
| **Član 117** | Sadržaj evidencije | Podaci o identitetu, transakciji, vrsti, valuti, svrsi, itd. |
| **Član 127** | Čuvanje podataka | Minimum 5 godina od prestanka odnosa. |
| **Član 131–134** | Nadzor | Ministarstvo i FIU vrše nadzor. |
| **Član 137–138a** | Prekršaji | Kazne od 5.000 do 20.000 EUR za pravna lica. |

---

## 20. Resursi i linkovi

- **FIU – Črnogorska Finansijsko-obavještajna jedinica:** https://fiu.gov.me
  - Registri: CRS, CRPS, PEP, stvarni vlasnici.
  - Platforma za prijave.

- **Centralni registar stanovništva (CRS):** https://crs.gov.me
- **Centralni registar privrednih subjekata (CRPS):** https://crps.gov.me
- **Zakon o sprečavanju pranja novca (tekst):** `/home/razzee/agera-knowledge/extracted-text/Zakon o sprečavanju pranja novca i finansiranja terorizma.txt`
- **Oficijalni elektrončki dnevnik (Sl. List Crne Gore):** https://www.sluzbenilist.me

---

**Ovi AJL se oslanja na Montenegrin AML zakon. Za pitanja tumačenja obratiti se stručnjaku za finansijski zakone.**
