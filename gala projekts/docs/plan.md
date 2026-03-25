# Expense Tracker — Projekta plāns

## A. Programmas apraksts

Šī programma ir izdevumu uzskaites rīks, kas ļauj lietotājam pievienot, apskatīt, filtrēt, analizēt un eksportēt savus izdevumus.  
Programma palīdz sekot līdzi personīgajiem tēriņiem, sadalot tos pa kategorijām un laika periodiem.

Lietotājs var:
- pievienot jaunus izdevumus
- apskatīt visus ierakstus
- filtrēt pēc mēneša
- redzēt kopsavilkumu pa kategorijām
- dzēst ierakstus
- eksportēt datus CSV formātā

---

## B. Datu struktūra

Viens izdevuma ieraksts tiek attēlots kā vārdnīca .json failā:

- id: 1  
- date: 2025-03-01  
- amount: 12.50  
- category: Ēdiens  
- description: Pusdienas

## Paskaidrojums

Projekts ir sadalīts vairākos moduļos, lai nodrošinātu skaidru struktūru un atbildību sadalījumu.

- `storage.py` nodarbojas ar datu saglabāšanu un ielādi no faila, nodrošinot persistenci.
- `logic.py` satur visas biznesa loģikas funkcijas, piemēram, pievienošanu, dzēšanu, filtrēšanu un aprēķinus.
- `app.py` atbild par lietotāja mijiedarbību, izvēlņu attēlošanu un ievades apstrādi.
- `export.py` nodrošina datu eksportu CSV formātā.

Šāda modulāra pieeja ļauj vieglāk uzturēt kodu, atkārtoti izmantot funkcijas un atdalīt lietotāja interfeisu no biznesa loģikas.

## C. Moduļu plāns

### storage.py

Atbild par datu saglabāšanu un ielādi no JSON faila.

Funkcijas:
- `load_expenses()` — nolasa datus no JSON faila; ja fails neeksistē, atgriež tukšu sarakstu  
- `save_expenses(expenses)` — saglabā izdevumu sarakstu JSON failā  

---

### logic.py

Satur biznesa loģiku bez lietotāja ievades un failu operācijām.

Funkcijas:
- `add_expense(expenses, date, amount, category, description)` — pievieno jaunu izdevumu ar unikālu ID  
- `delete_expense(expenses, expense_id)` — dzēš izdevumu pēc ID  
- `filter_by_month(expenses, year, month)` — filtrē izdevumus pēc norādītā gada un mēneša  
- `sum_total(expenses)` — aprēķina visu izdevumu kopējo summu  
- `sum_by_category(expenses)` — sagrupē izdevumus pa kategorijām un aprēķina summas  
- `get_available_months(expenses)` — atgriež unikālos mēnešus formātā YYYY-MM  

---

### app.py

Atbild par lietotāja mijiedarbību (CLI).

- Izvēlnes attēlošana  
- Lietotāja ievades apstrāde  
- Funkciju izsaukšana no `logic.py` un `storage.py`  
- Datu attēlošana lietotājam  

---

### export.py

Atbild par datu eksportēšanu CSV formātā.

Funkcijas:
- `export_to_csv(expenses, filepath)` — eksportē izdevumu sarakstu uz CSV failu ar kolonām: datums, summa, kategorija, apraksts  

---

## D. Lietotāja scenāriji

1. Lietotājs pievieno izdevumu ar korektiem datiem → programma pievieno ierakstu un saglabā to failā.  

2. Lietotājs ievada nepareizu datumu → programma parāda kļūdas paziņojumu un pieprasa ievadi atkārtoti.  

3. Lietotājs izvēlas skatīt izdevumus, bet saraksts ir tukšs → programma informē, ka nav pieejamu datu.  

4. Lietotājs filtrē izdevumus pēc mēneša → programma parāda attiecīgos ierakstus un kopējo summu.  

## E. Robežgadījumi

- Ja `expenses.json` neeksistē → programma atgriež tukšu sarakstu un turpina darbību  
- Ja JSON fails ir bojāts → programma var atgriezt tukšu sarakstu vai apstrādāt kļūdu  
- Ja lietotājs ievada nepareizu datuma formātu → tiek parādīts kļūdas paziņojums  
- Ja lietotājs ievada negatīvu vai nederīgu summu → tiek parādīta kļūda un pieprasīta atkārtota ievade  
- Ja izvēlnē ievada nederīgu opciju → programma pieprasa ievadi vēlreiz  
- Ja saraksts ir tukšs un lietotājs izvēlas skatīt datus → tiek parādīts informatīvs paziņojums  
- Ja CSV fails jau eksistē → tas tiek pārrakstīts ar jaunajiem datiem  