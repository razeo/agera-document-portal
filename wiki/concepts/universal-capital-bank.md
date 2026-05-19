# Universal Capital Bank (koncept)

## Opšte informacije

**Universal Capital Bank** je banka sa sjedištem u Podgorici, Crna Gora. Banka nudi međunarodne platne usluge, uključujući primanje osnivačkog kapitala iz inostranstva.

### Ključni podaci
- **Naziv:** Universal Capital Bank AD
- **Sjedište:** Stanka Dragojevića bb, Podgorica, Crna Gora
- **SWIFT/BIC:** `UNCBMEPG`
- **IBAN:** `ME25560005000000100457`
- **Valuta:** EUR (Euro)
- **Kontakt:** +382 20 481 407, international@ucbank.me, www.ucbank.me

## SWIFT/BIC kod (UNCBMEPG)

**UNCBMEPG** je jedinstveni SWIFT (Society for Worldwide Interbank Financial Telecommunication) identifikator za Universal Capital Bank. SWIFT kod se sastoji iz:
- **Bank code (4 slova):** UCB (Universal Capital Bank)
- **Country code (2 slova):** ME (Montenegro)
- **Location code (2 slova/cifre):** MP (Podgorica)
- **Branch code (3 slova/cifre):** G (glavna/održava se prazno za matičnu banku)

## Uloga u međunarodnim platnim sredstvima

Kao **"Creditor Agent"** (Field 58), Universal Capital Bank prima direktna ili posredovana sredstva sa inostranstva za osnivački kapital.

## Korespondentska banka

Kada se sredstva šalju iz inostranstva, koristi se **OTP BANK PLC.** kao posredna (korespondentska) banka:

| Banka                | SWIFT/BIC | Adresa                          | Uloga        |
|----------------------|-----------|----------------------------------|--------------|
| Universal Capital Bank | UNCBMEPG  | Stanka Dragojevića bb, Podgorica | Creditor Agent |
| OTP Bank PLC         | OTPVHUHB  | Nador Street 16, Budapest, Hungary | Intermediary Agent |

## Upute za korisnike

Kada šaljete sredstva Universal Capital Banku iz inostranstva:

1. **SWIFT adresa** – Pošiljaoc mora navesti `UNCBMEPG` kao korespondentsku banku.
2. **IBAN** – `ME25560005000000100457`
3. **Ime primaoca** – `UNIVERSAL CAPITAL BANK AD`
4. **Adresa** – `Stanka Dragojevića bb, Podgorica, Crna Gora`
5. **Reference** – Obavezno navesti: `Founding capital - (Details of the transaction – invoice no, contract no etc.)`

## Reference
- Universal Capital Bank, Podgorica – SWIFT UNCBMEPG, IBAN ME25560005000000100457
- ISO 9362 (SWIFT/BIC standard)
- ISO 13616 (IBAN standard)
- Međunarodna platna sistema: TARGET2, SEPA

---

*Ovaj dokument sadrži konceptualne informacije o Universal Capital Banku. Za detaljne instrukcije, pogledati `wiki/raw-sources/ucb-instructions.md`.*


## 📋 Instrukcije za uplate (iz: ucb-instrukcije-2)

## 🔍 Instrukcije (ekstrahovano)

```text
STANDARD SETTLEMENT INSTRUCTION
(Currency: EUR )

Intermediary Agent – BIC
SWIFT Code
Bank Name
Bank Address

OTPVHUHB
OTP BANK PLC.
NADOR STREET 16, BUDAPEST, HUNGARY

Creditor Agent – BIC
SWIFT Code
Bank Name
Bank Address

UNCBMEPG
UNIVERSAL CAPITAL BANK
STANKA DRAGOJEVICA BB, PODGORICA, ME

Creditor – Name & Address

IBAN
Account Name
Address

ME25560005000000100457
UNIVERSAL CAPITAL BANK AD
STANKA DRAGOJEVICA BB, PODGORICA
CRNA GORA

Remittance Information – this field is mandatory
Founding capital - (Details of the transaction – invoice no, contract no etc.)

Universal Capital Bank
International Payments Department
Stanka Dragojevića bb
Podgorica, Montenegro
Tel:
+ 382 20 481 407
E-mail: international@ucbank.me
Web:
www.ucbank.me


```

> Dokument je možda dugačak. Sačuvan je samo prvi dio zbog veličine.

