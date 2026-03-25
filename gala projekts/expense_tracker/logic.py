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


# =========================
# ANALYTICS
# =========================

def filter_by_month(expenses, year, month):
    target = f"{year}-{month}"
    result = []

    for exp in expenses:
        if exp["date"][:7] == target:
            result.append(exp)

    return result


def sum_total(expenses):
    total = 0

    for exp in expenses:
        total += exp["amount"]

    return total


def sum_by_category(expenses):
    totals = {}

    for exp in expenses:
        category = exp["category"]

        if category not in totals:
            totals[category] = 0

        totals[category] += exp["amount"]

    return totals


def get_available_months(expenses):
    months = set()

    for exp in expenses:
        month = exp["date"][:7]  # YYYY-MM
        months.add(month)

    return sorted(months)

