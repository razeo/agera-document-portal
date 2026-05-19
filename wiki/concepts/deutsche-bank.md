# Deutsche Bank (koncept)

## Opšte informacije

**Deutsche Bank AG** je jedna od vodećih globalnih investicionih banaka s sjedištem u Frankfurtu na Majni, Njemačka. Osnovana je 1870. godine i deluje kao međunarodna finansijska institucija pružajuća širok spektar usluga: investiciono bankarstvo, poslovno bankarstvo, upravljanje imovinom i trgovanje.

### Ključni podaci
- **Naziv:** Deutsche Bank AG
- **Sjedište:** Frankfurt am Main, Germany
- **SWIFT/BIC:** `DEUTDEFF`
- **Lei:** 7LTWFZYICNSX8D621K86
- **Kontakt:** +49 69 9100-00

## SWIFT/BIC kod (DEUTDEFF)

**DEUTDEFF** je jedinstveni SWIFT (Society for Worldwide Interbank Financial Telecommunication) identifikator za Deutsche Bank AG Frankfurt. SWIFT kod se sastoji od:
- **Bank code (4 slova):** DEUT (Deutsche Bank)
- **Country code (2 slova):** DE (Germany)
- **Location code (2 slova/ cifre):** FF (Frankfurt Main)
- **Branch code (3 slova/cifre, opcionalno):** obično prazan za glavnu banku

### Kako se koristi
Kod DEUTDEFF služi za:
- Međunarodne wire transfer (SWIFT MT103 poruke)
- Korespondentski obračun između banaka
- Identifikaciju poslovne jedinice Frankfurt za međunarodne transakcije

## Uloga u međunarodnim platnim sredstvima

Kao **"Account with Institution"** (Field 57), Deutsche Bank Frankfurt učestvuje kao posredna banka (correspondent bank) u lancu plaćanja. Kada se sredstva šalju iz trećih zemalja ka Crnogorskoj komercijalnoj banci (CKB), koristi se Deutsche Bank Frankfurt kao prolazna tačka zbog:
1. Velike mreže korespondenskih računa
2. Efikasne obraćanja u EUR valuti
3. Pouzdanog multilateralnog netting sistema

## Deutsche Bank u regionu

U istočnoj evropi i Balkanu, Deutsche Bank poseduje:
- **Deutsche Bank AG** ( Frankfurt) – matična banka
- **Deutsche Bank d.d.** Zagreb, Hrvatska (retired)
- **Deutsche Bank International S.A.** Luksemburg – pruža usluge za region
- **Podružnice:** Beograd, Sarajevo, Skopje (uklonečene ili pretvorene)

U **Crnoj Gori**, CKB ima korespondentski odnos sa Deutsche Bankom kako bi primala/šaljala međunarodne uplate.

## Upute za korisnike

Kada primalac (npr. CKB) traži da pošiljalac koristi Deutsche Bank:

1. **SWIFT adresa** – Pošiljaoc mora navesti `DEUTDEFF` kao posrednu banku.
2. **IBAN i SWIFT CKB-a** – Konkretan račun i SWIFT `CKBCMEPG`.
3. **Korektne reference** – Održavati tačan opis transakcije (Field 70, 72).
4. **Valuta** – EUR je preferirana valuta za ovu rutu.

## Povezane banke i šifre

| Banka                | SWIFT/BIC   | Lokacija          | Valuta  | Party Identifier       |
|----------------------|-------------|-------------------|---------|------------------------|
| Deutsche Bank AG     | DEUTDEFF    | Frankfurt/Main    | EUR     | 10093630450000         |
| Deutsche Bank Trust  | BKTRUS33    | New York          | USD     | 04456267               |
| Crnogorska Komercijalna Banka | CKBCMEPG | Podgorica | EUR     | DE60500700100936304500 |

## Reference
- Deutsche Bank AG, Frankfurt – Swift DEUTDEFF, BIC 2078
- ISO 9362 (SWIFT/BIC standard)
- Međunarodna platna sistema: TARGET2, SEPA

---

*Ovaj dokument sadrži konceptualne informacije o Deutsche Banku i njegovoj ulozi u međunarodnim platnim transakcijama sa CKB. Za detaljne instrukcije, pogledati `wiki/raw-sources/deutsche-bank-instructions.md`.*


## 📋 Instrukcije za uplate (iz: deutsche-bank-ckb)

## 🔍 Instrukcije

### Podaci za uplatu
- **CKB** (Crnogorska Komercijalna Banka)
- **SWIFT Code**: Treba provjeriti u originalnom dokumentu
- **IBAN**: Treba provjeriti u originalnom dokumentu
- **Reference**: DOO ime i svrha uplate

### Field 70 (Opis plaćanja)
- Naziv drustva koji se osniva
- Svrha: Osnivacki kapital
- Ime uplatioca

