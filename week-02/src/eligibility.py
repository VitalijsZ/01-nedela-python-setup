while True:
    age_input = input("Ievadi vecumu: ") 
    try:
        # Ievadi vecumu: 20
        age = int(age_input)
        if age < 1 or age > 120:
            print("Lūdzu ievadi vecumu no 1 līdz 120") 
        else:
            break #valid input goes to next step
    except ValueError:
        print("Lūdzu ievadi skaitli!")


# Vai ir autovadītāja apliecība? (j/n): n
while True:
    auto = input("Vai ir autovadītāja apliecība? (j/n): ").lower()
    if auto in ("j", "n"):
        break
    print("Lūdzu ievadi tikai 'j' vai 'n'")
# Vai ir students? (j/n): j
while True:
    student = input("Vai ir students? (j/n): ").lower()
    if student in ("j", "n"):
        break
    print("Lūdzu ievadi tikai 'j' vai 'n'")
# Vai ir veterāns? (j/n): n
while True:
    veteran = input("Vai ir veterāns? (j/n): ").lower()
    if veteran in ("j", "n"):
        break
    print("Lūdzu ievadi tikai 'j' vai 'n'")
print("---")

# Balsošana
if age >= 18:
    balsosana = "Balsošana:        Jā ✓"
else:
    balsosana = "Balsošana:        Nē ✗"
# Auto īre
if age >= 21 and auto == "j": 
    ire = "Auto īre:         Jā ✓"
elif age >= 21 and auto == "n":
    ire = "Auto īre:         Nē ✗ (nav apliecības)"
else:
    ire = "Auto īre:         Nē ✗"
# Senioru atlaide
if age >= 65 or veteran == "j":
    senioru_atlaide = "Senioru atlaide:  Jā ✓"
else:
    senioru_atlaide = "Senioru atlaide:  Nē ✗"
# Studentu atlaide
if 16 <= age <=26 and student == "j":
    studentu_atlaide = "Studentu atlaide: Jā ✓"
else:
    studentu_atlaide = "Studentu atlaide: Nē ✗"

print(f"{balsosana}\n{ire}\n{studentu_atlaide}\n{senioru_atlaide}")