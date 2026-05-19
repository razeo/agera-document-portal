# [[lovcen-banka]]

> **Lovćen Banka AD Podgorica** — instrukcje za uplate osnivačkog kapitala iz inostranstva
> **Kategorija:** bank
> **Izvor:** Obavještenje o instrukcijama za uplate osnivačkog kapitala iz inostranstva Lovćen Banka AD Podgorica
> **Poslednje ažuriranje:** 2026-05-03

## 📋 Sažetak

Lovćen Banka AD Podgorica prima uplate osnivačkog kapitala iz inostranstva preko SWIFT mreže. Ključni podaci: SWIFT/BIC `LOVBMEPGXXX`, IBAN `ME25 5650 0500 0000 0008 07`. Intermediary bank: Raiffeisen Bank International AG (`RZBAATWW`). Korisnik mora da navede "Founding Capital" + ime kompanije u polju 70.

## 🔍 Detalji

### Bankovni identifikatori
- **Naziv banke:** Lovćen Banka AD Podgorica
- **SWIFT/BIC:** `LOVBMEPGXXX`
- **IBAN (beneficiary):** `ME25 5650 0500 0000 0008 07`

### Intermediate Bank (Field 56A)
- **Raiffeisen Bank International AG**
- **SWIFT:** `RZBAATWW`

### Correspondent Banks (po valuti)
| Valuta | Banka | SWIFT |
|--------|-------|-------|
| EUR, USD, CHF | Raiffeisen Bank International AG | RZBAATWW |
| EUR | Privredna Banka Zagreb | PBZGHR2X (IBAN HR9623400091970015109) |
| EUR | Bayerische Landesbank | BYLADEMM |
| EUR | Landesbank Baden-Württemberg | SOLADEST |

### Field 70 (Payment Details)
Obavezan tekst: **"Founding Capital" + Ime osnivačke kompanije**. Nije eksplicitno naveden u originalu, ali je standardna praksa.

## 🔗 Povezani koncepti
- [[adriatic-bank]] — slična procedura za drugu banku
- [[deutsche-bank]] — CKB IBAN obrađen u Deutsche Banku
- [[centralni-registar]] — nakon uplate, registracija u CRPS

## ⚠️ Kontradikcije / Nejasnoće
- [ ] Potrebno proveriti: Da li Lovćen Banka traži dodatne dokumente (SWIFT copy, bankarski račun osnivača)?
- [ ] Da li postoji limit minimalnog iznosa za strane uplate?

## 📚 Izvori
- [[lovcen-bank-instructions]] — Originalna bankarska instrukcija

## 📝 Istorija promena
- `2026-05-03` — Inicijalna generacija iz ekstrahovanog teksta


## 📋 Instrukcije za uplate (iz: lovcen-bank-instrukcije-2)

## 🔍 Instrukcije (ekstrahovano)

```text
INCOMING PAYMENT INSTRUCTION

56A: Intermediary bank / Correspondent bank
Swift Address:

RZBAATWW

Name & Address:

RAIFFEISEN BANK INTERNATIONAL AG
VIENNA,

57A: Account with Institution / Beneficiary’s Bank
Party Identifier:

001-55.097.455 EUR

Swift Address:

LOVBMEPGXXX

Name & Address:

Lovcen Banka AD Podgorica
Bulevar Knjaza Danila Petrovića, 13/32, I sprat
81000, Montenegro

59: Beneficiary Customer
IBAN

ME25 5650 0500 0000 0008 07

Name & Address:

LOVCEN BANKA AD
BUL.KNJAZA DANILA PETROVIĆA
81000 PODGORICA

LIST OF MAIN CORRESPONDENTS OF LOVCEN BANKA AD

Currency

Correspondent Bank

Correspondent SWIFT/BIC Account no.

EUR

RAIFFEISEN BANK INTERNATIONAL
RZBAATWW
AG

001-55.097.455

USD

RAIFFEISEN BANK INTERNATIONAL
RZBAATWW
AG

070-55.097.455

CHF

RAIFFEISEN BANK INTERNATIONAL
RZBAATWW
AG

073-55.097.455

EUR

PRIVREDNA BANKA ZAGREB D.D.

PBZGHR2X

HR66234000919700151
09

EUR

BAYERISCHE LANDESBANK,
MUENCHEN

BYLADEMM

0000006324553

INCOMING PAYMENT INSTRUCTION
Currency

Correspondent Bank

Correspondent SWIFT/BIC Account no.

EUR

LANDESBANK BADENWUERTTEMBERG

SOLADEST

2811950


```

> Dokument je možda dugačak. Sačuvan je samo prvi dio zbog veličine.

