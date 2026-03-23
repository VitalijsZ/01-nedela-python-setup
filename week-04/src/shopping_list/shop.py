import sys
from storage import load_list, save_list
from utils import (
    is_valid_price,
    is_valid_qty,
    calc_line_total,
    calc_grand_total,
    count_units
    )


def main():
    if len(sys.argv) < 2:
        print("Lietošana: add/list/total/clear")
        return

    command = sys.argv[1]

    # ========= ADD =========
    if command == "add":
        if len(sys.argv) < 5:
            print("Lietošana: add <nosaukums> <daudzums> <cena>")
            return

        name = sys.argv[2]
        qty_input = sys.argv[3]
        price_input = sys.argv[4]

        if not is_valid_price(price_input):
            print("Kļūda: cena nav derīga.")
            return
        
        if not is_valid_qty(qty_input):
            print("Kļūda: daudzumam jābūt pozitīvam skaitlim.")
            return
        
        qty = int(qty_input)
        price = float(price_input)

        items = load_list()

        new_item = {
            "name": name,
            "qty": qty,
            "price": price
        }

        items.append(new_item)
        save_list(items)

        line_total = calc_line_total(new_item)

        print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR")

    # ========= LIST =========
    elif command == "list":
        items = load_list()

        if not items:
            print("Saraksts ir tukšs.")
            return

        print(f"\nIepirkumu saraksts ({len(items)} produkti):\n")

        for i, item in enumerate(items, start=1):            
            line_total = calc_line_total(item) 

            print(f"{i}. {item['name']} × {item['qty']} — "
                f"{item['price']:.2f} EUR/gab. — {line_total:.2f} EUR"
            )

    # ========= TOTAL =========
    elif command == "total":
        items = load_list()

        if not items:
            print("Saraksts ir tukšs.")
            return
        
        total_price = calc_grand_total(items)
        total_units = count_units(items)

        print(
            f"Kopā: {total_price:.2f} EUR "
            f"({total_units} vienības, {len(items)} produkti)"
        )

    # ========= CLEAR =========
    elif command == "clear":
        save_list([])
        print("Saraksts iztīrīts.")

    else:
        print("Nezināma komanda.")
        

if __name__ == "__main__":
    main()

