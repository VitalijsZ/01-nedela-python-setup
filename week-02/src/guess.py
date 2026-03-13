from random import randint
# Galvenais spēles cikls
while True:
    random_number = randint(1,100)    
    counter = 0
    # Viena spēle
    while True:
        # Minējumu cikls
        guess_input = input("Tavs minējums: ")     
        try:
            # Ievadi skaitli
            guess = int(guess_input)
            counter += 1                  
            if guess == random_number or counter == 10:
                if guess == random_number:
                    print(f"Tu vinnēji. Slēptais skaitlis bija {random_number}. Meģinājumu skaits: {counter}")
                else:
                    print(f"Tu zaudēji. Slēptais skaitlis bija {random_number}.")
                break     
            elif guess > random_number:
                print("Par lielu")
            else:
                print("Par mazu")     
        except ValueError:
            print("Lūdzu ievadi skaitli!")
    # Dod cilvekam izveli vai viņš grib spēlēt vēlreiz?
    while True:
        spelet_velreiz = input("Spēlēt vēlreiz? (j/n): ").lower()
        if spelet_velreiz in ("j", "n"):
            break
        print("Lūdzu ievadi tikai 'j' vai 'n'")
    if spelet_velreiz == "n":
        break

