import sys

# Validacija: parbaudam, vai N ir padots ka arguments
if len(sys.argv) < 2:
    print("Please provide N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be an integer (number)")
    sys.exit(1)

output = []

# FizzBuzz
for number in range (1, N + 1):
    if number % 3 == 0 and number % 5 == 0:
        # Pirmam kartam parbaudam dalamibu ar abiem
        output.append("FizzBuzz")
    elif number % 3 == 0:
        output.append("Fizz")
    elif number % 5 == 0:
        output.append("Buzz")
    elif number % 7 == 0:
        output.append("Jazz")
    else:
        # Ja dalamiba neattiecas, pievienojam pasu skaitli
        output.append(str(number))

# Rezultata izvade ka viena rinda ar komatiem
result = ", ".join(output)
print(result)