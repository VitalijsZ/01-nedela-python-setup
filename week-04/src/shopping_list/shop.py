import sys
from storage import load_data, save_data
from utils import is_valid_price

def main():
    if len(sys.argv) < 2:
        print("Lietošana: add/list")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print("Lietošana: add <nosaukums> <cena>")
            return

        name = sys.argv[2]
        price_input = sys.argv[3]

        if not is_valid_price(price_input):
            print("Kļūda: cena nav derīga.")
            return
        price = float(price_input)

        items = load_data()

        items.append({
            "name": name,
            "price": price
        })

        save_data(items)

        print(f"✓ Pievienots: {name} ({price} EUR)")

    elif command == "list":
        items = load_data()

        if not items:
            print("Saraksts ir tukšs.")
            return

        print("Iepirkumu saraksts:")

        for i, item in enumerate(items, start=1):
            print(f"{i}. {item.get('name')} — {item.get('price'):.2f} EUR")

    elif command == "total":
        items = load_data()

        if not items:
            print("Saraksts ir tukšs.")
            return
        total = 0
        count = len(items)
        for item in items:
            total += item.get("price", 0)            
        print(f"Kopā: {total:.2f} EUR ({count} produkti)")     

    elif command == "clear":
        save_data([])
        print("Saraksts iztīrīts.")
        

if __name__ == "__main__":
    main()

