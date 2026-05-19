# Deutsche Bank - Instrukcije za uplate iz inostranstva

## Izvorni dokument

**Dokument:** Obavještenje o instrukcijama za uplate osnivačkog kapitala iz inostranstva Deutsche Bank sa CKB IBAN računom

**Status:** POVJERLJIVO / CONFIDENTIAL

## Banke i šifre

### Pošiljalac / Sending Bank
- **Ime:** Deutsche Bank AG Frankfurt/Main, Germany
- **SWIFT/BIC adresa:** `DEUTDEFF`
- **Valuta:** EUR (Euro)

### Primalac / Receiving Bank (CKB)
- **Ime:** Crnogorska komercijalna banka AD Podgorica
- **SWIFT/BIC adresa:** `CKBCMEPG`
- **IBAN račun:** `DE60500700100936304500`
- **Adresa:** Moskovska bb, 20000 Podgorica, Crna Gora
- **Kontakt:** CKB Call Centar 19894, Fax: +382/20/235 757, E-mail: info@ckb.me, www.ckb.me

## SWIFT polja (MT103 format)

### Field 57 - Account with Institution
Banka koja šalje sredstva (Deutsche Bank Frankfurt):
```
SWIFT: DEUTDEFF
Ime: Deutsche Bank AG Frankfurt/Main, Germany
```

### Field 58 - Beneficiary Institution
Banka primalac (CKB) - podaci o računu:
```
IBAN: DE60500700100936304500
SWIFT: CKBCMEPG
Ime: CRNOGORSKA KOMERCIJALNA BANKA AD PODGORICA
```

### Field 72 – Sender to Receiver Information
Dodatne informacije za primalca:
```
2925062 - 88
```

## Proces uplate - koraci

1. **Iniciranje uplate** – Pošiljalac (investitor iz inostranstva) pokreće international transfer preko Deutsche Banka (DEUTDEFF).

2. **Navedenje podataka CKB-a** – U SWIFT poruci (MT103) postaviti:
   - Field 57: DEUTDEFF (Deutsche Bank)
   - Field 58: IBAN DE60500700100936304500 + SWIFT CKBCMEPG
   - Field 72: 2925062 - 88 (ako se traži referenca)

3. **Dodatne reference** – Ukoliko se uplata odnosi na osnivački kapital ili specifični projekat, u polje 72 ili u referencu za primalca dodati:
   - Broj/sifrа načelnu (npr. 2925062)
   - Dodatni identifikator (npr. -88)

4. **CKB prijem** – CKB prihvata sredstva na IBAN račun DE60500700100936304500 i procesira ih unutar banke, raspoređujući na odgovarajuće interne račune ovisno o valuti i namjeni.

## Važne napomene

- **Račun je u Montenegro** – Iako IBAN započinje sa "DE" (Njemačka), zbog CKB-ove strukture računa u sistemu, IBAN je vezan za Crnogorsku komercijalnu banku.
- **Valuta** – Glavna valuta je EUR; moguće su i druge valute putem CKB mreže.
- **Kontakt** – Za pitanja vezana za primanje sredstava, obratiti se CKB Call Centru 19894 ili info@ckb.me.

## Reference

- SWIFT direktorij: Deutsche Bank (DEUTDEFF), CKB (CKBCMEPG)
- IBAN standard: ISO 13616
- SWIFT MT103: Standard za korespondentsku banku

---

*Napomena: Ovaj dokument služi kao pregled procedurê i ne zamenjuje zvanične bankarske uputstva. Uvek potvrditi tačnost podataka sa bankom pre slanja sredstava.*
