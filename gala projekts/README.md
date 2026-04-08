# Izdevumu izsekotājs

Komandrindas Python lietojums personīgo izdevumu uzskaitei, analīzei un eksportam uz CSV failu.

---

## 1. Projekta apraksts

Šī programma ļauj lietotājam pievienot, apskatīt, filtrēt, analizēt un dzēst izdevumus.  
Tā palīdz sekot līdzi personīgajiem tēriņiem un sadalīt tos pa kategorijām un mēnešiem.

---

## 2. Uzstādīšana

1. Atveram Command Prompt.
2. Izvēlamies direktoriju, kur vēlamies saglabāt programmu: cd direktorija_ceļš (Piemērs: cd C:\Users\VitalijsZ)
3. Izpildām komandu: git clone https://github.com/VitalijsZ/01-nedela-python-setup.git
4. Pārejam uz expense_tracker mapi. (Piemērs: cd C:\Users\VitalijsZ\01-nedela-python-setup\gala projekts\expense_tracker)
5. Palaižam programmu ar komandu: python app.py

Nav nepieciešamas papildus bibliotēkas — nepieciešams tikai Python 3.10+.

---

## 3. Lietošana

Programma darbojas interaktīvā režīmā ar izvēlni:

1) Pievienot izdevumu  
2) Parādīt izdevumus  
3) Filtrēt pēc mēneša  
4) Kopsavilkums pa kategorijām  
5) Dzēst izdevumu  
6) Eksportēt CSV  
7) Iziet  

Lietotājs izvēlas darbību, ievada nepieciešamos datus un programma izvada rezultātu.

---

## 4. Funkcionalitāte

- Izdevumu pievienošana ar validāciju  
- Datu saglabāšana JSON failā  
- Filtrēšana pēc mēneša  
- Kopsummas aprēķins  
- Kopsavilkums pa kategorijām  
- Izdevumu dzēšana  
- CSV eksportēšana  

---

## 5. Projekta struktūra

- `app.py` — lietotāja saskarne (CLI)  
- `logic.py` — biznesa loģika  
- `storage.py` — datu ielāde un saglabāšana  
- `export.py` — CSV eksports  
- `expenses.json` — datu fails  

---

## 6. Autors

Vitalijs Z — Programmēšanas pamati, 2026

---