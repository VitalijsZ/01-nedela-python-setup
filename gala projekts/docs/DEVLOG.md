# Izstrādes žurnāls

---

## 1. solis: Projekta plānošana

Sākumā izveidoju projekta struktūru un sadalīju kodu pa moduļiem (storage, logic, export, app). 
Sapratu, ka tas palīdzēs uzturēt kodu tīrāku un vieglāk paplašināmu.
Grūtākais bija izvēlēties, kā organizēt funkcijas logic.py.

---

## 2. solis: Datu slānis

Izveidoju storage.py ar JSON datu ielādi un saglabāšanu.
Izveidoju iespēju pievienot izdevumus ar datumu, summu, kategoriju un aprakstu.
Sākumā bija problēmas ar faila ceļu, bet tās atrisināju, izmantojot os.path.
Sākumā nezināju par funkciju datetime.strptime(), kas ļauj pārbaudīt datuma formātu.
To iemācījos izmantot, lai validētu lietotāja ievadīto datumu (YYYY-MM-DD).
Iemācījos, ka .strip() metode noņem liekos atstarpes no ievades sākuma un beigām.
Uzzināju arī par funkciju sorted(), kas ļauj sakārtot sarakstu, piemēram, mēnešus augošā secībā.
Iemācījos strādāt ar failu lasīšanu un rakstīšanu Python.

---

## 3. solis: Filtrēšana un analīze

Papildināju logic.py ar filtrēšanu pēc mēneša, kopsummām un dzēšanu.
Sarežģītākais bija pareizi apstrādāt datumus un grupēt datus pa kategorijām.

---

## 4. solis: CSV eksports un dokumentācija

Izveidoju export.py un pievienoju CSV eksportēšanas funkcionalitāti.
Papildināju app.py ar lietotāja izvēlni eksportam.
Grūtības bija ar CSV formatēšanu, bet to atrisināju ar csv moduli.

---