from storage import load_expenses, save_expenses
from logic import add_expense, delete_expense

def main():
    expenses = load_expenses()

    while True:
        command = input("Enter command (add/list/delete/exit): ")

        if command == "add":
            # ievade + add_expense
            date = input("Date (YYYY-MM-DD): ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            expenses = add_expense(expenses, date, amount, category, description)
            save_expenses(expenses)            

        elif command == "list":
            if not expenses:
                
                print("Saraksts ir tukšs.")

            else:
                print(f"ID   Datums       Summa      Kategorija  Apraksts \n"
                        f"------------------------------------------------------- ")
                    # izdrukā sarakstu
                for exp in expenses:
                    print(f"{exp['id']:<3} | {exp['date']:<10} | {exp['amount']:<10} | {exp['category']:<10} | {exp['description']}")
                    
                print(f"------------------------------------------------------- ")
                

        elif command == "delete":
            # dzēšana pēc ID
            expense_id = int(input("Enter ID to delete: "))
            found = False

            for exp in expenses:
                if exp["id"] == expense_id:
                    found = True
                    break
            if not found:
                print("Expense not found.")
            else:
                expenses = delete_expense(expenses, expense_id)
                save_expenses(expenses)
            

        elif command == "exit":
            break


if __name__ == "__main__":
    main()