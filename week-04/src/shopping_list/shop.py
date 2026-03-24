import sys

# Importējam funkcijas no storage.py (failu darbības)
from storage import load_list, save_list, get_price, set_price

# Importējam palīgfunkcijas no utils.py (validācija + aprēķini)
from utils import (
    is_valid_qty,
    is_valid_price,
    calc_line_total,
    calc_grand_total,
    count_units
)


def main():
    # Pārbaudām vai vispār ir nodota komanda
    if len(sys.argv) < 2:
        print("Lietošana: add/list/total/clear")
        return

    # Komanda (add, list, total, clear)
    command = sys.argv[1]

    # ========= ADD =========
    if command == "add":

        # Pārbaudām vai ir pietiekami argumenti
        if len(sys.argv) < 4:
            print("Lietošana: python shop.py add <nosaukums> <daudzums>")
            return

        # Iegūstam produkta nosaukumu un daudzumu (string formātā)
        name = sys.argv[2]
        qty_input = sys.argv[3]

        # Validējam daudzumu
        if not is_valid_qty(qty_input):
            print("Kļūda: daudzumam jābūt pozitīvam skaitlim.")
            return

        # Konvertējam uz int
        qty = int(qty_input)

        # Meklējam cenu datubāzē
        price = get_price(name)

        # ===== JA CENA ATRASTA =====
        if price is not None:
            print(f"Atrasta cena: {price:.2f} EUR/gab.")

            # Cikls izvēlei A/M
            while True:
                choice = input("[A]kceptēt / [M]ainīt? > ").lower()

                # Ja akceptē cenu
                if choice == "a":
                    break

                # Ja lietotājs grib mainīt cenu
                elif choice == "m":

                    # Iekšējais cikls cenas ievadei
                    while True:
                        new_price_input = input("Jaunā cena (vai Enter lai atceltu): > ").strip()

                        # Ja lietotājs atceļ
                        if new_price_input == "":
                            print("Cenas maiņa atcelta.")
                            break

                        # Validējam cenu
                        if is_valid_price(new_price_input):
                            price = float(new_price_input)

                            # Saglabājam jauno cenu datubāzē
                            set_price(name, price)

                            print(f"✓ Cena atjaunināta: {name} → {price:.2f} EUR")
                            break
                        else:
                            print("Kļūda: nederīga cena. Mēģini vēlreiz.")

                    # Iziet no A/M cikla
                    break

                else:
                    print("Nederīga izvēle, mēģini vēlreiz.")

        # ===== JA CENA NAV ATRASTA =====
        else:
            print("Cena nav zināma.")

            # Prasām cenu līdz ievade ir derīga
            while True:
                price_input = input("Ievadi cenu: > ")

                if is_valid_price(price_input):
                    price = float(price_input)
                    break

                print("Kļūda: nederīga cena.")

            # Saglabājam jauno cenu datubāzē
            set_price(name, price)

            print(f"✓ Cena saglabāta: {name} ({price:.2f} EUR)")

        # ===== SAGLABĀ IEPIRKUMU SARAKSTĀ =====

        # Ielādē esošos datus no faila
        items = load_list()

        # Izveido jaunu ierakstu
        new_item = {
            "name": name,
            "qty": qty,
            "price": price
        }

        # Pievieno sarakstam
        items.append(new_item)

        # Saglabā atpakaļ JSON failā
        save_list(items)

        # Aprēķina rindas summu
        line_total = calc_line_total(new_item)

        # Izvada apstiprinājumu
        print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR")

    # ========= LIST =========
    elif command == "list":

        # Ielādē visus produktus
        items = load_list()

        # Ja tukšs saraksts
        if not items:
            print("Saraksts ir tukšs.")
            return

        print(f"\nIepirkumu saraksts ({len(items)} produkti):\n")

        # Izvada katru produktu
        for i, item in enumerate(items, start=1):
            line_total = calc_line_total(item)

            print(
                f"{i}. {item['name']} × {item['qty']} — "
                f"{item['price']:.2f} EUR/gab. — {line_total:.2f} EUR"
            )

    # ========= TOTAL =========
    elif command == "total":

        # Ielādē datus
        items = load_list()

        if not items:
            print("Saraksts ir tukšs.")
            return

        # Kopējā summa
        total_price = calc_grand_total(items)

        # Kopējais vienību skaits
        total_units = count_units(items)

        # Izvada rezultātu
        print(
            f"Kopā: {total_price:.2f} EUR "
            f"({total_units} vienības, {len(items)} produkti)"
        )

    # ========= CLEAR =========
    elif command == "clear":

        # Notīra failu (saglabā tukšu sarakstu)
        save_list([])

        print("Saraksts iztīrīts.")

    # Ja komanda nav atpazīta
    else:
        print("Nezināma komanda.")


# Programmas entry point
if __name__ == "__main__":
    main()