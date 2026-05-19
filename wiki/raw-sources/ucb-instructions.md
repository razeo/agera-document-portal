# Universal Capital Bank - Instrukcije za uplate iz inostranstva

## Izvorni dokument

**Dokument:** Obavještenje o instrukcijama za uplate osnivačkog kapitala iz inostranstva Universal Capital Bank

**Status:** POVJERLJIVO / CONFIDENTIAL

## Banke i šifre

### Intermediary Agent (Korespondentska banka)
- **Ime:** OTP BANK PLC.
- **SWIFT/BIC adresa:** `OTPVHUHB`
- **Adresa:** Nador Street 16, Budapest, Hungary

### Creditor Agent (Primač banka)
- **Ime:** UNIVERSAL CAPITAL BANK
- **SWIFT/BIC adresa:** `UNCBMEPG`
- **Adresa:** Stanka Dragojevića bb, Podgorica, ME

### Creditor (Konačni primalac/račun)
- **IBAN:** `ME25560005000000100457`
- **Ime računa:** `UNIVERSAL CAPITAL BANK AD`
- **Adresa:** Stanka Dragojevića bb, Podgorica, Crna Gora

## SWIFT polja (MT103 format)

### Field 57 - Account with Institution (Intermediary Agent)
```
SWIFT: OTPVHUHB
Ime: OTP BANK PLC.
Adresa: NADOR STREET 16, BUDAPEST, HUNGARY
```

### Field 58 - Beneficiary Institution (Creditor Agent)
```
SWIFT: UNCBMEPG
Ime: UNIVERSAL CAPITAL BANK
Adresa: STANKA DRAGOJEVICA BB, PODGORICA, ME
```

### Field 59 - Beneficiary Account (Creditor)
```
IBAN: ME25560005000000100457
Ime: UNIVERSAL CAPITAL BANK AD
Adresa: STANKA DRAGOJEVICA BB, PODGORICA, CRNA GORA
```

### Field 70 – Remittance Information (OBAVEZNO)
```
Founding capital - (Details of the transaction – invoice no, contract no etc.)
```

## Proces uplate - koraci

1. **Iniciranje uplate** – Pošiljaoc (investitor iz inostranstva) pokreće internacionalni transfer preko svoje banke.

2. **Navedenje podataka UCB-a** – U SWIFT poruci (MT103) postaviti:
   - **Intermediary Agent (Field 57):** OTPVHUHB – OTP BANK PLC.
   - **Creditor Agent (Field 58):** UNCBMEPG – Universal Capital Bank
   - **Beneficiary Account (Field 59):** ME25560005000000100457

3. **Remittance Reference** – U polje 70 (Remittance Information) obavezno navesti:
   - `Founding capital - (Details of the transaction – invoice no, contract no etc.)`

4. **UCB prijem** – Universal Capital Bank prihvata sredstva na IBAN račun ME25560005000000100457.

## Važne napomene

- **Valuta** – Valuta transakcije je EUR (Euro).
- **Namen sredstava** – Sredstva se odnose na osnivački kapital.
- **Kontakt** – Za pitanja vezana za primanje sredstava:
  - Tel: +382 20 481 407
  - E-mail: international@ucbank.me
  - Web: www.ucbank.me

## Reference
- SWIFT direktorij: Universal Capital Bank (UNCBMEPG), OTP Bank (OTPVHUHB)
- IBAN standard: ISO 13616
- SWIFT MT103: Standard za korespondentsku banku
- TARGET2 sustav za EU/EEA platne transakcije

---

*Napomena: Ovaj dokument služi kao pregled procedure i ne zamenjuje zvanične bankarske uputstva. Uvek potvrditi tačnost podataka sa bankom pre slanja sredstava.*
