#Constants
# Kilometrus ↔ judzes (1 km = 0.621371 mi)
KM_TO_MI = 0.621371
#Kilogramus ↔ marcinas (1 kg = 2.20462 lb)
KG_TO_LB = 2.20462
#Litrus ↔ galonus (1 L = 0.264172 gal)
L_TO_GAL = 0.264172
#Dolari ↔ Eiro (1 $ = 0.84235020 €)
USD_TO_EUR = 0.84235020




while True:
    conversion = input("Choose a conversion: 1) km<->mi 2) kg<->lb 3) L<->gal 4) USD<->EUR:\n")
    if conversion not in ("1", "2", "3", "4"):
        print("Plese enter number from 1 to 4") 
    else:
        break #valid input goes to next step

if conversion == "1":
    direction_text = "Direction: 1) km -> mi 2) mi -> km\n"
    factor_forward = KM_TO_MI
    factor_backward = 1/KM_TO_MI
    units = ("km", "mi")        
elif conversion == "2":
    direction_text = "Direction: 1) kg -> lb 2) lb -> kg\n"
    factor_forward = KG_TO_LB
    factor_backward = 1/KG_TO_LB
    units = ("kg", "lb")        
elif conversion == "3":
    direction_text = "Direction: 1) L -> gal 2) gal -> L\n"
    factor_forward = L_TO_GAL
    factor_backward = 1/L_TO_GAL
    units = ("L", "gal")        
elif conversion == "4":
    direction_text = "Direction: 1) $ -> € 2) € -> $\n"
    factor_forward = USD_TO_EUR
    factor_backward = 1/USD_TO_EUR
    units = ("USD", "EUR")        

while True:
    direction = input(direction_text)
    if direction not in ("1", "2"):
        print("You need to choose from 1 to 2")                      
    else:
        break

if direction == "1":
    factor = factor_forward
    unit_from = units[0]
    unit_to = units[1]
else:   
    factor = factor_backward         
    unit_from = units[1]
    unit_to = units[0]
while True:
    try:
        value = float(input("Enter value: "))
        break
    except ValueError:
        print("Please enter a numeric value")
result = value * factor
print(f"{value:.2f} {unit_from} = {result:.2f} {unit_to}")

