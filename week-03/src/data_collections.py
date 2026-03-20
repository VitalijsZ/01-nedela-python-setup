# A daļa — Saraksts ar skaitļiem

# Izveidojam sarakstu ar skaitļiem
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializējam mainīgos manuālai summas un vidējās vērtības aprēķināšanai
total = 0
count = 0
even_numbers = []

# Iterējam cauri sarakstam
for i in numbers:
    total += i
    count += 1

    # Filtrējam pāra skaitļus
    if i % 2 == 0:
        even_numbers.append(i)

# Aprēķinām vidējo vērtību ar drošības pārbaudi
if count > 0:
    average = total / count
else:
    average = 0

# Rezultātu izvade
print("--- Saraksti ---")
print(f"Skaitļi: {numbers}")
print(f"Summa: {total}, Vidējais: {average}")
print(f"Pāra skaitļi: {even_numbers}")

# Slicing piemēri
print(f"Pirmie 3: {numbers[:3]}, Pēdējie 2: {numbers[-2:]}")
print(f"Katrs otrais elements: {numbers[::2]}")


# B daļa — Vārdnīca ar studentiem

# Izveidojam vārdnīcu ar studentiem un viņu atzīmēm
students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95      
}

print("--- Vārdnīcas ---")

# Izvadām sākotnējo vārdnīcu
# print(f"Sākotnējais studentu saraksts: {students}")

# Pievienojam jaunu studentu
students["John"] = 85

# Izvadām pēc pievienošanas
# print(f"Studentu saraksts ar jauno studentu: {students}")

# Mainām esoša studenta atzīmi
students.update({"Anna": 99})

# Izvadām pēc izmaiņām
# print(f"Annai jauna atzīme: {students}")

# Inicializējam mainīgos labākā studenta meklēšanai
highest_score = None
best_name = None

# Iterējam cauri vārdnīcai
for name, score in students.items():
    print(f"{name}: {score}")

    # Salīdzinām, lai atrastu augstāko atzīmi
    if highest_score is None or score > highest_score:
        highest_score = score
        best_name = name

# Izvadām rezultātu
print(f"Labākais students: {best_name} ({highest_score})")

# Filtrējam studentus ar atzīmi >= 80
print("--- Studenti ar atzīmi >= 80 ---")

# Izveidojam tukšu sarakstu, kur glabāsies filtrētie studenti
# Katrs elements būs vārdnīca ar "name" un "grade"
filtered_students = []

# Iterējam cauri visiem studentiem vārdnīcā
for name, score in students.items():
    
    # Pārbaudām, vai studenta atzīme atbilst nosacījumam
    if score >= 80:
        
        # Pievienojam studentu kā dict jaunajā sarakstā
        filtered_students.append({"name": name, "grade": score})

# Izmantojam enumerate, lai piešķirtu numerāciju (sākot no 1)
for i, student in enumerate(filtered_students, start=1):
    
    # Izvadām formatētu rezultātu:
    # i — kārtas numurs
    # student["name"] — studenta vārds
    # student["grade"] — atzīme
    print(f"{i}. {student['name']} — {student['grade']}")




