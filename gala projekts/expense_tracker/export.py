import csv

def export_to_csv(expenses, filename="expenses.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # header
        writer.writerow(["date", "amount", "category", "description"])

        # data
        for exp in expenses:
            writer.writerow([
                exp["date"],
                exp["amount"],
                exp["category"],
                exp["description"]
            ])