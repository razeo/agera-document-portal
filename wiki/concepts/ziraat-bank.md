# Ziraat Bank Montenegro AD

## Osnovni podaci

| **Naziv banke** | ZIRAAT BANK MONTENEGRO AD PODGORICA |
|---|---|
| **SWIFT / BIC** | `TCZBMEPG` |
| **IBAN** | `ME25 5750 0500 0000 0008 42` |
| **Adresa** | Ulica Slobode 84, 81000 Podgorica, Crna Gora |
| **Web** | www.ziraatbank.com.tr |

## Instrukcije za uplate osnivačkog kapitala iz inostranstva

### Procedura uplate

Za uplatu osnivačkog kapitala iz inostranstva (non-SEPA) koristiti sledeće podatke u SWIFT porudžbini:

```
57A: Account with institution:
     SWIFT: TCZBMEPG
     Bank Name: ZIRAAT BANK MONTENEGRO AD
     Address: Ulica Slobode 84
     City/Country: 81000 Podgorica, Montenegro

59: Beneficiary customer:
     IBAN: ME25575005000000000842
     Client name: ZIRAAT BANK MONTENEGRO
     Address: Ulica Slobode 84
     Place: 81000 Podgorica

70: Remittance Information:
     Founding Capital (dodati ime kompanije)
```

### Korespondent banke (intermediary banks)

Ziraat Bank Montenegro koristi sledeće korespondent banke za prikupljanje sredstava iz različitih valuta:

| **SWIFT** | **Banka** | **Grad** | **Valuta** |
|-----------|-----------|----------|------------|
| `TCZBTR2A` | Turkiye Cumhuriyeti Ziraat Bankasi A.S. | Ankara, Turska | EUR, USD, TRY |
| `TCZBDEFF` | Ziraat Bank International AG | Frankfurt am Main, Nemačka | EUR |
| `KTAGDEFF` | KT Bank AG | Frankfurt am Main, Nemačka | EUR |
| `RZBAATWW` | Raiffeisen Bank International | Vienna, Austrija | EUR |

## Važne napomene

- **Polje 70** mora sadržati tekst "Founding Capital" i ime kompanije čiji se kapital uplaćuje.
- Sredstva se direktno smještaju na račun Ziraat Bank Montenegro AD (IBAN: `ME25575005000000000842`).
- Za SEPA uplate možete koristiti direktno IBAN bez korespondent banke.
- Za non-SEPA uplate, sredstva prolaze kroz jednu od korespondent banki navedenih iznad.

## Vezani koncepti

- [[centralni-registar]] - Banke i uplate
- [[registracioni-broj]] - Registracioni broj
- [[pdv]] - Poreski sistem Crne Gore i MEK

## Izvor

Dokument: *Obavještenje o instrukcijama za uplate osnivačkog kapitala iz inostranstva ZIRAAT BANK MONTENEGRO AD PODGORICA*


## 📋 Instrukcije za uplate (iz: ziraat-bank-instrukcije-2)

## 🔍 Instrukcije (ekstrahovano)

```text
INCOMING PAYMENT INSTRUCTION

56 INTERMEDIARY:

TURKIYE CUMHURIYETI ZIRAAT BANKASI A.S.

ANKARA, TURKEY
SWIFT CODE: TCZBTR2A
(EUR, USD,TRY)

56 INTERMEDIARY:

ZIRAAT BANK INTERNATIONAL AG

FRANKFURT AM MAIN
SWIFT CODE: TCZBDEFF
(EUR)

56 INTERMEDIARY:

KT BANK AG
FRANKFURT AM MAIN
SWIFT CODE: KTAGDEFF
(EUR)

56 INTERMEDIARY:

RAIFFEISEN BANK INTERNATIONAL
VIENNA AUSTRIA
SWIFT CODE: RZBAATWW
(EUR)

57 ACCOUNT WITH INSTITUTION:

ZIRAAT BANK MONTENEGRO AD

ULICA SLOBODE 84
81000 PODGORICA
MONTENEGRO
SWIFT CODE: TCZBMEPG

59 BENEFICIARY CUSTOMER:

IBAN :

NAME:
ADDRESS:
PLACE:

ME25575005000000000842
ZIRAAT BANK MONTENEGRO
ULICA SLOBODE 84
81000 PODGORICA


```

> Dokument je možda dugačak. Sačuvan je samo prvi dio zbog veličine.

