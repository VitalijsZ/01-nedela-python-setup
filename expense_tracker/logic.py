# =========================
# ID GENERATION
# =========================

def get_next_id(expenses):
    """
    Atgriež nākamo unikālo ID.
    """
    if not expenses:
        return 1

    max_id = 0

    for exp in expenses:
        if exp["id"] > max_id:
            max_id = exp["id"]

    return max_id + 1


# =========================
# EXPENSE OPERATIONS
# =========================

def add_expense(expenses, date, amount, category, description):
    """
    Pievieno jaunu izdevumu sarakstam.

    Atgriež updated expenses list.
    """

    new_expense = {
        "id": get_next_id(expenses),
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(new_expense)

    return expenses


def delete_expense(expenses, expense_id):
    """
    Dzēš izdevumu pēc ID.

    Atgriež jaunu sarakstu bez izvēlētā izdevuma.
    """

    new_expenses = []

    for exp in expenses:
        if exp["id"] != expense_id:
            new_expenses.append(exp)

    return new_expenses