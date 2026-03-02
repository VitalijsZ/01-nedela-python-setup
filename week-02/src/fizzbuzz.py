output = []

for number in range (1, 16):
    if number % 3 == 0 and number % 5 == 0:
        output.append("FizzBuzz")
    elif number % 3 == 0:
        output.append("Fizz")
    elif number % 5 == 0:
        output.append("Buzz")
    elif number % 7 == 0:
        output.append("Jazz")
    else:
        output.append(str(number))

result = ", ".join(output)
print(result)