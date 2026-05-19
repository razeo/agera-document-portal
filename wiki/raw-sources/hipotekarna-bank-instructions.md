# Hipotekarna Banka - Instrukcije za uplate osnivačkog kapitala iz inostranstva

## Procedura uplate

Za uplatu osnivačkog kapitala iz inostranstva (non-SEPA) koristiti sledeće podatke u SWIFT porudžbini:

```
57A: Account with institution:
     SWIFT: HBBAMEPGXXX
     Bank Name: Hipotekarna banka ad
     Address: Podgorica, Montenegro

59: Beneficiary customer:
     IBAN: ME25520000000116810094
     Client name: HIPOTEKARNA-RN ZA OSNIVACKI ULOG
     Address: Josipa Broza Tita br. 67, Podgorica, Montenegro

70: Remittance Information:
     Payment reference: [obavezan opis - npr. "Founding Capital" i ime kompanije]
```

### Napomena za polje 70
- Polje 70 (Remittance Information) **mora** sadržati tekst "Founding Capital" (ili "Osnivački ulog") i **ime kompanije** čiji se kapital uplaćuje.

## Korespondent banke

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

- Za **SEPA uplate** koristiti direktno IBAN (`ME25520000000116810094`) bez korespondent banke.
- Za **non-SEPA uplate**, sredstva prolaze kroz odgovarajuću korespondent banku iz gornje tabele, zavisno od valute.
- Sredstva se direktno smještaju na račun HIPOTEKARNA-RN ZA OSNIVACKI ULOG (IBAN: ME25520000000116810094).
- U polju 70 obavezno navedi: "Founding Capital - [Ime kompanije]" (ili ekvivalent na lokalnom jeziku: "Osnivački ulog - [Ime kompanije]").

## Izvor

Dokument: *Obavještenje o instrukcijama za uplate osnivačkog kapitala iz inostranstva HIPOTEKARNA BANKA*
