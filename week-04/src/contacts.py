import json
import sys
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež []."""
    if not os.path.exists(CONTACTS_FILE):
        return []

    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_contacts(contacts):
    """Saglabā kontaktu sarakstu JSON failā."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)


def add_contact(name, phone):
    contacts = load_contacts()

    contacts.append({
        "name": name,
        "phone": phone
    })

    save_contacts(contacts)

    print(f"✓ Pievienots: {name} ({phone})")       


def list_contacts():
    contacts = load_contacts()

    if not contacts:
        print("Nav kontaktu.")
        return

    print("Kontakti:")

    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c.get('name')} — {c.get('phone')}")


def search_contacts(query):
    contacts = load_contacts()

    results = []

    for c in contacts:
        if query.lower() in c.get("name", "").lower():
            results.append(c)

    if not results:
        print("Nav atrastu kontaktu.")
        return

    print(f"Atrasti {len(results)} kontakti:")

    for i, c in enumerate(results, start=1):
        print(f"{i}. {c.get('name')} — {c.get('phone')}")


def main():
    if len(sys.argv) < 2:
        print("Lietošana: add/list/search")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print("Lietošana: add <name> <phone>")
            return

        name = sys.argv[2]
        phone = sys.argv[3]
        add_contact(name, phone)

    elif command == "list":
        list_contacts()

    elif command == "search":
        if len(sys.argv) < 3:
            print("Lietošana: search <name>")
            return

        query = sys.argv[2]
        search_contacts(query)

    else:
        print("Nezināma komanda:", command)


if __name__ == "__main__":
    main()