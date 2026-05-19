# Hipotekarna Banka AD Podgorica

## Osnovni podaci

| | |
|---|---|
| **Naziv banke** | HIPOTEKARNA BANKA AD PODGORICA |
| **SWIFT / BIC** | `HBBAMEPGXXX` |
| **Adresa** | Podgorica, Crna Gora |
| **Specifična jedinica** | HIPOTEKARNA-RN ZA OSNIVACKI ULOG (Račun za osnivački ulog) |
| **Adresa računa** | Josipa Broza Tita br. 67, Podgorica, Crna Gora |

## Instrukcije za uplate osnivačkog kapitala iz inostranstva

### Procedura uplate

Za uplatu osnivačkog kapitala iz inostranstva (non-SEPA) koristiti sledeće podatke u SWIFT porudžbini:

```
57A: Account with institution:
     SWIFT: HBBAMEPGXXX
     Bank Name: Hipotekarna banka ad
     Address: Podgorica, Montenegro

59A: Beneficiary customer:
     IBAN: ME25520000000116810094
     Client name: HIPOTEKARNA-RN ZA OSNIVACKI ULOG
     Address: Josipa Broza Tita br. 67, Podgorica, Montenegro

70A: Payment reference:
     [Obavezan tekst - npr. "Founding Capital - [Ime kompanije]"]
```

### Korespondent banke

Za prikupljanje sredstava iz različitih valuta, Hipotekarna Banka koristi sledeće korespondent banke:

| SWIFT | Banka | Grad | Valuta |
|-------|-------|------|--------|
| BYLADEMM | Bayerische Landesbank, München | München | EUR |
| GIBAATWG | Erste Group Bank AG | Vienna | USD/EUR |
| BBRUBEBB | ING Belgium NV/SA (formerly Bank BR) | Brussels | EUR |
| BCITITMM | Intesa Sanpaolo SPA | Milano | EUR |
| SOLADEST | Landesbank Baden-Württemberg | Stuttgart | EUR |
| RZBAATWW | Raiffeisen Bank International AG | Vienna | GBP/CHF/USD/EUR |

## Važne napomene

- Polje **70 (Remittance Information)** mora sadržati tekst "Founding Capital" (ili "Osnivački ulog") i **ime kompanije** čiji se kapital uplaćuje.
- Sredstva se direktno smještaju na račun HIPOTEKARNA-RN ZA OSNIVACKI ULOG (IBAN: `ME25520000000116810094`).
- Za **SEPA uplate** koristiti direktno IBAN bez korespondent banke.
- Za **non-SEPA uplate**, sredstva prolaze kroz korespondent banku iz tabele, zavisno od valute.

## Vezani koncepti

- [[pdv]] - Poreski sistem Crne Gore i MEK
- [[doo]] - Društvo sa ograničenom odgovornošću
- [[poreska-prijava]] - Ročenja i obaveze
- [[adriatic-bank]] - Adriatic Bank AD Podgorica (za poređenje procedura)

## Izvor

Dokument: *Obavještenje o instrukcijama za uplate osnivačkog kapitala iz inostranstva HIPOTEKARNA BANKA*


## 📋 Instrukcije za uplate (iz: hipotekarna-bank-instrukcije-2)

## 🔍 Instrukcije (ekstrahovano)

```text
[P1-INTERNO]

INSTRUCTIONS FOR INCOMING PAYMENT IN FAVOR OF CLIENTS OF HIPOTEKARNA BANKA:

57A: Account with institution ( SWIFT / BIC) : HBBAMEPGXXX
Hipotekarna banka ad, Podgorica, Montenegro
59A: Beneficiary customer (IBAN): ME25520000000116810094
HIPOTEKARNA-RN ZA OSNIVACKI ULOG, JOSIPA BROZA TITA BR.67,
PODGORICA, MONTENEGRO

70A: Payment reference:

Usage of the field 70 is mandatory !

You are kindly requested to choose one of the following correspondent banks from the
LIST OF MAIN CORRESPONDENTS OF HIPOTEKARNA BANKA AD
Currency

Bank

City

SWIFT/BIC

EUR

BAYERISCHE LANDESBANK,
MUENCHEN

MUENCHEN

BYLADEMM

USD/EUR

ERSTE GROUP BANK AG

VIENNA

GIBAATWG

EUR

ING BELGIUM NV/SA
(FORMERLY BANK BR

BRUSSELS

BBRUBEBB

EUR

INTESA SANPAOLO SPA

MILANO

BCITITMM

EUR

LANDESBANK BADENWUERTTEMBERG

STUTTGART

SOLADEST

GBP/CHF/USD/EUR

RAIFFEISEN BANK
INTERNATIONAL AG

VIENNA

RZBAATWW


```

> Dokument je možda dugačak. Sačuvan je samo prvi dio zbog veličine.

