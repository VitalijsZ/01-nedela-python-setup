from storage import load_expenses, save_expenses
from logic import add_expense, delete_expense
from logic import filter_by_month, sum_by_category, sum_total, get_available_months
from export import export_to_csv

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
    expenses = load_expenses()

    while True:
        print("""
        1) Pievienot izdevumu
        2) Parādīt izdevumus
        3) Filtrēt pēc mēneša
        4) Kopsavilkums pa kategorijām
        5) Dzēst izdevumu
        6) Eksportēt CSV
        7) Iziet
        """)
        choice = input("Izvēlies darbību (1-7): ")
        if not choice.isdigit():
            print("Kļūda: jāievada cipars!")
            continue
        # 1) Pievienot izdevumu
        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Kļūda: jāievada skaitlis!")
                continue

            print("\nKategorija:")
            for i, cat in enumerate(CATEGORIES, 1):
                print(f"  {i}) {cat}")

            cat_choice = input("Izvēlies kategoriju: ")

            if not cat_choice.isdigit():
                print("Kļūda: jāievada cipars!")
                continue

            cat_index = int(cat_choice)

            if cat_index < 1 or cat_index > len(CATEGORIES):
                print("Kļūda: nepareiza izvēle!")
                continue

            category = CATEGORIES[cat_index - 1]

            description = input("Description: ")

            print(f"\n✓ Pievienots: {date} | {category} | {amount:.2f} EUR | {description}")

            expenses = add_expense(expenses, date, amount, category, description)
            save_expenses(expenses)    


        # 2) Parādīt izdevumus
        elif choice == "2":
            if not expenses:
                
                print("Saraksts ir tukšs.")

            else:
                print(f"ID   Datums       Summa          Kategorija     Apraksts \n"
                        f"------------------------------------------------------- ")
                    # izdrukā sarakstu
                for exp in expenses:
                    print(f"{exp['id']:<3} | {exp['date']:<10} | {exp['amount']:<8.2f} EUR | {exp['category']:<10} | {exp['description']}")
                    
                print(f"------------------------------------------------------- ")

                total = sum_total(expenses)

                print(f"\nKopā: {total:.2f} EUR ({len(expenses)} ieraksti)")


        # 3) Filtrēt pēc mēneša
        elif choice == "3":
            months = get_available_months(expenses)

            print("\nPieejamie mēneši:")
            for i, m in enumerate(months, 1):
                print(f"{i}) {m}")

            choice_month = int(input("Izvēlies mēnesi: "))

            selected_month = months[choice_month - 1]

            year = selected_month[:4]
            month = selected_month[5:]

            filtered = filter_by_month(expenses, year, month)

            print(f"\n{selected_month} izdevumi:\n")

            for exp in filtered:
                print(f"{exp['date']} | {exp['amount']} EUR | {exp['category']} | {exp['description']}")

            print(f"\nKopā: {sum_total(filtered)} EUR ({len(filtered)} ieraksti)")

        # 4) Kopsavilkums pa kategorijām
        elif choice == "4":
            totals = sum_by_category(expenses)
            total_sum = sum_total(expenses)

            if not totals:
                print("Nav datu.")
                continue

            print("\nKopsavilkums pa kategorijām:\n")

            for category, amount in totals.items():
                print(f"{category}: {amount:.2f} EUR")

            print("\n----------------------")
            print(f"KOPĀ: {total_sum:.2f} EUR")

        # 5) Dzēst izdevumu
        elif choice == "5":
            if not expenses:
                print("Nav izdevumu.")
                continue

            print("\nIzdevumi:\n")

            for i, exp in enumerate(expenses, 1):
                print(f"{i}) {exp['date']} | {exp['amount']} EUR | {exp['category']} | {exp['description']}")

            choice_delete = int(input("\nIzvēlies numuru dzēšanai: "))

            if choice_delete < 1 or choice_delete > len(expenses):
                print("Kļūda: nepareiza izvēle!")
                continue

            # paņem pareizo expense
            selected_expense = expenses[choice_delete - 1]
            expense_id = selected_expense["id"]

            # dzēš pēc ID (iekšēji)
            expenses = delete_expense(expenses, expense_id)
            save_expenses(expenses)

            print("✓ Ieraksts dzēsts.")

        # 6) Eksportēt CSV
        elif choice == "6":
            export_to_csv(expenses)
            print("CSV fails veiksmīgi eksportēts: expenses.csv")


        # 7) Iziet
        elif choice == "7":
            break


if __name__ == "__main__":
    main()