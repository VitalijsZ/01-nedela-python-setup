from storage import load_expenses, save_expenses
from export import export_to_csv
from datetime import datetime
from logic import (
    add_expense,
    delete_expense,
    filter_by_month,
    sum_by_category,
    sum_total,
    get_available_months
)

# Kategoriju saraksts
CATEGORIES = [
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits",
]


def main():
    # Ielādē datus no JSON faila
    expenses = load_expenses()

    while True:
        # ====== IZVĒLNE ======
        print("""
        1) Pievienot izdevumu
        2) Parādīt izdevumus
        3) Filtrēt pēc mēneša
        4) Kopsavilkums pa kategorijām
        5) Dzēst izdevumu
        6) Eksportēt CSV
        7) Iziet
        """)

        choice = input("Izvēlies darbību (1-7): ").strip()

        # Validācija — jāievada cipars
        if not choice.isdigit():
            print("Kļūda: jāievada cipars!")
            continue

        # =========================
        # 1) PIEVIENOT IZDEVUMU
        # =========================
        if choice == "1":

            # Datuma validācija
            while True:
                date = input("Datums (YYYY-MM-DD): ")

                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Kļūda: nepareizs datuma formāts! Mēģini vēlreiz.")

            # Summa
            while True:
                try:
                    amount = float(input("Summa (EUR): "))
                    if amount <= 0:
                        print("Kļūda: summai jābūt pozitīvai!")
                        continue
                    break
                except ValueError:
                    print("Kļūda: jāievada skaitlis! Mēģini vēlreiz.")

            # Kategorijas izvēle
            print("\nKategorija:")
            for i, cat in enumerate(CATEGORIES, 1):
                print(f"  {i}) {cat}")

            while True:
                cat_choice = input("Izvēlies kategoriju: ")

                if not cat_choice.isdigit():
                    print("Kļūda: jāievada cipars!")
                    continue

                cat_index = int(cat_choice)

                if 1 <= cat_index <= len(CATEGORIES):
                    category = CATEGORIES[cat_index - 1]
                    break
                else:
                    print("Kļūda: nepareiza izvēle!")

            # Apraksts
            while True:
                # Noņem liekās atstarpes no ievadītā teksta sākuma un beigām
                description = input("Apraksts: ").strip()
                if description:
                    break
                print("Kļūda: apraksts nedrīkst būt tukšs!")

            # Pievieno un saglabā
            expenses = add_expense(expenses, date, amount, category, description)
            save_expenses(expenses)

            print(f"\n✓ Pievienots: {date} | {category} | {amount:.2f} EUR | {description}")

        # =========================
        # 2) PARĀDĪT IZDEVUMUS
        # =========================
        elif choice == "2":

            if not expenses:
                print("Saraksts ir tukšs.")
                continue

            # Header
            print("ID   Datums       Summa      Kategorija     Apraksts")
            print("-" * 60)

            # Izdrukā visus izdevumus
            for exp in expenses:
                print(f"{exp['id']:<3} | {exp['date']:<10} | {exp['amount']:<8.2f} EUR | {exp['category']:<10} | {exp['description']}")

            print("-" * 60)

            # Kopējā summa
            total = sum_total(expenses)
            print(f"\nKopā: {total:.2f} EUR ({len(expenses)} ieraksti)")

        # =========================
        # 3) FILTRĒT PĒC MĒNEŠA
        # =========================
        elif choice == "3":

            months = get_available_months(expenses)

            if not months:
                print("Nav datu.")
                continue

            print("\nPieejamie mēneši:")
            for i, m in enumerate(months, 1):
                print(f"{i}) {m}")

            # Cikls līdz ievade ir pareiza
            while True:
                choice_month = input("Izvēlies mēnesi: ")

                if not choice_month.isdigit():
                    print("Kļūda: jāievada cipars!")
                    continue

                choice_month = int(choice_month)

                if 1 <= choice_month <= len(months):
                    break
                else:
                    print("Kļūda: nepareiza izvēle!")

            selected_month = months[choice_month - 1]

            # Sadalam selected_month uz gadu un menesi
            year, month = selected_month.split("-")

            filtered = filter_by_month(expenses, year, month)

            print(f"\n{selected_month} izdevumi:\n")

            for exp in filtered:
                print(f"{exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")

            print(f"\nKopā: {sum_total(filtered):.2f} EUR ({len(filtered)} ieraksti)")

        # =========================
        # 4) KOPSAVILKUMS
        # =========================
        elif choice == "4":

            totals = sum_by_category(expenses)

            if not totals:
                print("Nav datu.")
                continue

            print("\nKopsavilkums pa kategorijām:\n")

            for category, amount in totals.items():
                print(f"{category}: {amount:.2f} EUR")

            print("\n----------------------")
            print(f"KOPĀ: {sum_total(expenses):.2f} EUR")

        # =========================
        # 5) DZĒST IZDEVUMU
        # =========================
        elif choice == "5":

            if not expenses:
                print("Nav izdevumu.")
                continue

            print("\nIzdevumi:\n")

            for i, exp in enumerate(expenses, 1):
                print(f"{i}) {exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")

            choice_delete = input("\nKuru dzēst? (numurs vai 0 lai atceltu): ")
            if choice_delete == "0":
                print("Dzēšana atcelta.")
                continue

            if not choice_delete.isdigit():
                print("Kļūda: jāievada cipars!")
                continue

            choice_delete = int(choice_delete)

            if choice_delete < 1 or choice_delete > len(expenses):
                print("Kļūda: nepareiza izvēle!")
                continue

            # Atrodam ID un dzēšam
            selected_expense = expenses[choice_delete - 1]
            expense_id = selected_expense["id"]

            expenses = delete_expense(expenses, expense_id)
            save_expenses(expenses)

            print("✓ Ieraksts dzēsts.")

        # =========================
        # 6) CSV EKSPORTS
        # =========================
        elif choice == "6":

            filepath = input("Ievadi faila nosaukumu (piemēram: expenses.csv): ").strip()

            if not filepath:
                filepath = "expenses.csv"

            export_to_csv(expenses, filepath)

            print(f"CSV fails veiksmīgi eksportēts: {filepath}")

        # =========================
        # 7) IZIET
        # =========================
        elif choice == "7":
            print("Uz redzēšanos!")
            break


if __name__ == "__main__":
    main()