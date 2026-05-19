# AGERA Knowledge Base

> **AGERA d.o.o.** - Knjigovodstvene usluge, osnivanje preduzeća, poreski konsalting
> **Vlasnik:** Željko | **Osnovano:** Herceg Novi, Crna Gora
> **Zanu:** 17.07.1973

## Pregled

Ovaj wiki sadrži strukturirano znanje o:
- Poresko zakonodavstvo (CG + MEK)
- Klijenti (profili, industrie, specifičnosti)
- Usluge (knjigovodstvo, osnivanje, konsalting)
- Interni procesi (workflow, kontrolne liste)
- Softverski alati (OpenCode, Hermes, ERP)
- Rokovi i obaveze (poreski, statisticki, poslovni)

## Struktura znanja

raw-sources/ -> izvori (PDF, zakoni, transkripti)
wiki/ -> LLM-generisane sintetisane stranice
  concepts/ -> opšti koncepti (PDV,DOO, porez na dohodak)
  clients/ -> profil klijenata po sektoru
  services/ -> opis usluga koje AGERA nudi
  processes/ -> interni workflow-i i checkliste
  legislation/ -> pojedinacni zakoni/clanovi
  raw-sources/ -> Clean extracted text from originals (PDF->txt)
logs/ -> audit trail svih ingesta i promena

## Kako se koristi

1. Ingest - Dropuj izvor u raw-sources/ -> LLM azurira wiki
2. Query - Pitanje protiv wiki-a -> LLM sintezuje odgovor
3. Lint - Periodini health check: kontradikcije, orfani, gap-i

## Trenutni koncepti

### Legislativa
- [[odluka-naknade-registar]]
- [[pravila-osnivanja]]
- [[pravilnik-registar-subjekata]]
- [[pravilnik-registraciona-prijava]]
- [[pravilnik-registracioni-broj]]
- [[pravilnik-stvarni-vlasnici]]
- [[zakon-o-aml]]
- [[zakon-o-izmjenama-i-dopunama-zakona-o-pdv-2026]]
- [[zakon-o-pdv]]
- [[zakon-o-porezu-na-dobit]]
- [[zakon-o-privrednim-drustvima]]
- [[zakon-o-racunovodstvu]] - Zakon o računovodstvu (Crna Gora)

### Koncepti
- [[adriatic-bank]]
- [[akcionarsko-drustvo]]
- [[aml-pravilnik]] - procedurale detalje Zakona o sprečavanju pranja novca
- [[aml]]
- [[centralni-registar]]
- [[deutsche-bank]]
- [[direktor]]
- [[diskvalifikacija-direktora]]
- [[doo]]
- [[euid]]
- [[hipotekarna-banka]]
- [[imenovanje-direktora]]
- [[irms]]
- [[knjigovodstvo]]
- [[komanditno-drustvo]]
- [[kyc]]
- [[lovcen-banka]]
- [[naknade-registra]]
- [[nvo]]
- [[obrazac-prijave]]
- [[ortacko-drustvo]]
- [[pdv]]
- [[porez-na-dohodak]]
- [[preduzetnik]]
- [[prijava-sumnjivih-transakcija]]
- [[procedura-osnivanja-privrednog-drustva]]
- [[racunovodstvo]]
- [[registar-privrednih-subjekata]]
- [[registraciona-prijava]]
- [[registracioni-broj]]
- [[statut-ad]] - Statut akcionarskog društva (AD)
- [[statut-doo-jednoclano]] - Statut društva sa ograničenom odgovornošću — jednočlano
- [[stvarni-vlasnici]]
- [[ugovor-o-osnivanju-doo-viseclano]]
- [[ugovor-o-osnivanju-kd]]
- [[ugovor-o-osnivanju-od]]
- [[ugovor-osnivanja-doo]]
- [[ugovor-osnivanja-kd]]
- [[ugovor-osnivanja-od]]
- [[universal-capital-bank]]
- [[ustanova]]
- [[ziraat-bank]]

### Usluge
- [[aml-kompliance]]
- [[knjigovodstvo-nvo]]
- [[osnivanje-ad]]
- [[osnivanje-doo]]
- [[osnivanje-kd]]
- [[osnivanje-od]]
- [[osnivanje-overview]]
- [[osnivanje-preduzetnika]]
- [[osnivanje-ustanove]]
- [[poljoprivreda-usluge]] - Usluge za poljoprivredu, šumarstvo i ribarstvo
- [[preradivacka-industrija-usluge]] - Usluge za prerađivačku industriju
- [[saobracaj-skladistenje-usluge]]
- [[trgovina-usluge]] - Usluge za trgovinu na veliko i malo
- [[usluge-smjestaja-ishrane-usluge]] - Usluge za smještaj i ishranu

### Procesi
- [[appointing-director]]
- [[disqualification]]
- [[elektronska-registracija-doo]]
- [[evidencija-ovlascenih-lica]]
- [[izmjena-statuta]]
- [[poreska-prijava]]
- [[post-incorporation-compliance]]
- [[prestanak-drustva]]
- [[registracija-firme]] - Procedura registracije preduzeća (DOO)
- [[registracija-predmetka]]

### Izvori (Raw Sources)
- [[aml-extracted]]
- [[deutsche-bank-instructions]]
- [[hipotekarna-bank-instructions]]
- [[kd-a-extracted]]
- [[kd-a-poljoprivreda-sumarstvo-i-ribarstvo-extracted]] - POLJOPRIVREDA, ŠUMARSTVO I RIBARSTVO (KD A)
- [[kd-c-preradjivacka-industrija-extracted]]
- [[kd-g-trgovina-na-veliko-i-na-malo-extracted]]
- [[kd-h-saobracaj-i-skladistenje-extracted]]
- [[kd-i-usluge-smjestaja-i-ishrane-extracted]]
- [[kd-j-izdavacke-emiterske-i-djelatnosti-proizvodnje-i-distribucije-sadrzaja-extracted]]
- [[kd-l-finansijske-djelatnosti-i-djelatnosti-osiguranja-extracted]]
- [[kd-n-strucne-naucne-i-tehnicke-djelatnosti-extracted]]
- [[kd-o-administrativne-i-pomocne-usluzne-djelatnosti-extracted]]
- [[lovcen-bank-instructions]]
- [[registracija-firme-extracted]]
- [[statut-ad-extracted]]
- [[statut-doo-jednoclano-extracted]]
- [[ucb-instructions]]
- [[ugovor-osnivanja-doo-viseclano-extracted]]
- [[zakon-aml-extracted]]
- [[zakon-o-privrednim-drustvima-1-extracted]] - Zakon o privrednim društvima (Crna Gora)
- [[zakon-o-privrednim-drustvima-extracted]]
- [[zakon-o-racunovodstvu-84-25-extracted]]
- [[ziraat-bank-instructions]]


## Logovi

- logs/extraction-2026-05-03.md - Tekst ekstrakcija logovi
- logs/wiki-*.md - Individualni ingest logovi po dokumentu
- logs/ingest-2026-05-03.md - Kombinovani log (ukoliko postoji)

---

*Poslednje azuriranje: 2026-05-03 | AGERA Knowledge Base v0.1*
