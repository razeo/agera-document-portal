# Post-Incorporation Compliance — AGERA interni proces

> **Poslednje ažuriranje:** 2026-05-03
> **Odgovornost:** Knjigovodstveni konsalting tim (AGERA)
> **Cilj:** Kompletirati sve obaveze nakon osnivanja privrednog društva u Crnoj Gori

## 📋 Procesna mapa

```
[1. CRPS registracija gotova]
         |
         v
[2. IRMS evidencija] ← direktori/predstavnici
         |
         v
[3. Poreske prijave] ← PDV, PIT prijave
         |
         v
[4. Banka račun] ← otvaranje + potvrda banke
         |
         v
[5. Knjigovodstvo start] → nadogradnja servisa
```

---

## 🎯 Kada se koristi

Ovaj proces se aktivira **nakon što CRPS izda rješenje o registraciji** (PIB dodeljen). AGERA obavlja sledeće checked korake da klijent bude u potpunosti compliance.

---

## 📝 Početna provjera (pre CRPS)

Pre nego što podnesemo prijavu, proveriti:
- [ ] **Statut** je ovjeren i sadrži sve obavezne odredbe (organi, zastupanje, dobit)
- [ ] **Odluka/imena direktora/predstavnika** je spremna (ovjerena)
- [ ] **Potvrda banke o uplati kapitala** (ako je nova kompanija sa strane osnivače) — videti `[[lovcen-banka]]` upute
- [ ] **Rezervacija naziva** je aktivna (120 dana)

---

## ✅ Korak 1: IRMS evidencija (obavezna)

**Sistem:** IRMS (Integrirani Registar Mrežnih Servisa) — Poreska uprava

**Zašto:** Banke zahtevaju potvrdu iz IRMS-a da otvore račun. Takođe, za Poreske obaveze (PDV, PIT) je obavezan.

**Šta evidentirati:**
- **Direktor** (ime, prezime, JMBG, funkcija, datumimenovanja)
- **Ovlasceno lice za poslovanje** (ako nije isti direktor)
- **Clanovi odbora direktora** (ako postoji)

**Valuta:**


Krećem sa verifikacijom za domaće i strane osobe. Za domaće, koristim **e-trgovinu** portale. Za strane, tražim **ovjereni prevod** punomoćja. 

Krećem sa **kontrolnom listom** za svaki tip evidencije:

Za domaće osobe, koristim **portfolija poreskog obveznika** ili **sopstveni portfolio** za podnosioca. Za strane osobe, moram dostaviti **ovjereni prevod** i priložiti **digitalno potpisano ovlašćenje**. 

Počinjem sa **verifikacijom dokumenta** i prikupljanjem svih potrebnih info.


Isporavim **poverenje za zastupanje** i **digitalno potpisano ovlašćenje** kroz IRMS portal. 

Krećem sa **pravnom validacijom** dokumenta — proveravam da li su svi potpisi overeni i da li postoji **ovjereni prevod** za strane dokumente. Zatim, **podnosiću zahtev** preko **portfolija poreskog obveznika** ili **sopstvenog portfolija**, zavisno od statusa podnosioca.

Ažuriram **sistemske loge** i **čuvam potvrdu o evidentiranju** za klijenta i banku.

Zatim, prelazim na **poreske prijave** — **PDV i PIT** su ključni. Proveravam **prijavu PDV-a** ako je prihod prekoračio prag (18.000 EUR), inače registracija nije obavezna. 

Kod **poreske prijave za fizicka lica**, moram da koristim **Poresku prijavu (PIT)** sa prihoda od samozaposlenja. Za **pravna lica**, podnosim **Poresku prijavu (PIT)** sa prihoda od delatnosti. 

Sve ove prijave se podnose **elektronski** preko **eUprave** do **15. maja** za prethodnu godinu. Takođe, moram da **prijavim i doprinose** (zdravstveni, penzioni) za direktor a i zaposlene ako ih ima.

Ova蝦
Počinjem sa **bancim računom** — **obavezan korak** za svaku kompaniju. Za **strane osnivače**, koristim specifične banke koje primaju **uplate iz inostranstva** (Lovćen, Hipotekarna, Ziraat, UCB). 

Za **domaće osnivače**, otvaram račun u bilo kojoj banci. **Neophodni dokumenti**: 
- **Registarska dokumentacija** (izvod iz CRPS)
- **Odluč imenovanja direktora**
- **Potvrda iz IRMS-a** (za direktora/predstavnika)
- **Statut**

Nakon otvaranja računa, **čuvam potvrdu banke** o otvoranju i **apliaciraj tu informaciju u knjigovodstvo**. **Zatim**, **izvršim uplatu osnivačkog kapitala** ako nije već uplaćen.

**Krećem sa knjigovodstvom**: Nakon što sve registracije i banke budu gotove, **počnem sa knjigovodstvom** za AGERA servise. **Prvi korak**: **Početni inventar** (učitanje bilansa).

**Predajem klijentu**: Kada svi koraci budu kompletni, **predajem klijentu paket dokumenta**:
1. **Registarska dokumentacija** (izvod, potvrda)
2. **Statut** (overen)
3. **Bankovna dokumentacija** (potvrda o računu, uplati kapitala)
4. **IRMS potvrda**
5. **Poreske prijave** (PDV, PIT) — ako su podnete
6. **Knjigovodstveni izveštaj** (početno stanje)

**I ja za svaki korak logujem** u `logs/` (npr. `irms-evidencija-2026-05-03.md`, `poreske-prijave-2026-05-03.md`).

---

## 📋 Kontrolna lista (checklist)

### Nakon CRPS registracije
- [ ] IRMS evidencija za direktora/predstavnika (domaći/strani)
- [ ] Poreska prijava PDV (ako je obavezna)
- [ ] Poreska prijava PIT (za direktor a i zaposlene)
- [ ] Otvaranje bankovnog računa
- [ ] Uplata osnivačkog kapitala (ako nije ranije)
- [ ] Početno knjigovodstvo (učitavanje bilansa)
- [ ] Dokumentacija predata klijentu
- [ ] Svi logovi upisani u `logs/`

---

## 🔗 Povezani procesi
- [[registracija-predmetka]] — CRPS prijava i registracija
- [[evidencija-ovlascenih-lica]] — Detaljne IRMS procedura
- [[appointing-director]] — Imenovanje direktora
- [[osnivanje-doo]] — AGERA usluga kompletnog osnivanja
- [[pdv]] — Porez na dodatu vrijednost
- [[porez-na-dohodak]] — Porez na dohodak

---

*Ova stranica je generisana za AGERA internal use. Status: Draft v0.1.*
