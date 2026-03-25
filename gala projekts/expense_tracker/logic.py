from datetime import datetime

# =========================
# ID GENERATION
# =========================

def get_next_id(expenses):
    """
    Atgriež nākamo unikālo ID.
    """
    # Ja saraksts ir tukšs, sākam no 1
    if not expenses:
        return 1

    max_id = 0

    # Iziet cauri visiem izdevumiem un atrodam lielāko ID
    for exp in expenses:
        if exp["id"] > max_id:
            max_id = exp["id"]

    # Nākamais ID ir par 1 lielāks nekā maksimālais
    return max_id + 1


# =========================
# EXPENSE OPERATIONS
# =========================

def add_expense(expenses, date, amount, category, description):
    """
    Pievieno jaunu izdevumu sarakstam.
    Atgriež atjauninātu sarakstu.
    """

    # Izveido jaunu izdevuma objektu ar unikālu ID
    new_expense = {
        "id": get_next_id(expenses),
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    # Pievieno sarakstam
    expenses.append(new_expense)

    return expenses


def delete_expense(expenses, expense_id):
    """
    Dzēš izdevumu pēc ID.
    Atgriež jaunu sarakstu bez izvēlētā ieraksta.
    """

    new_expenses = []

    # Pievienojam tikai tos izdevumus, kuriem ID nesakrīt
    for exp in expenses:
        if exp["id"] != expense_id:
            new_expenses.append(exp)

    return new_expenses


# =========================
# ANALYTICS
# =========================

def filter_by_month(expenses, year, month):
    """
    Atgriež izdevumus, kuru datums ir norādītajā mēnesī.
    """

    result = []

    for expense in expenses:
        # Pārvērš string datumu par datetime objektu
        d = datetime.strptime(expense["date"], "%Y-%m-%d")

        # Salīdzina gadu un mēnesi
        if d.year == int(year) and d.month == int(month):
            result.append(expense)

    return result


def sum_total(expenses):
    """
    Aprēķina kopējo izdevumu summu.
    """

    total = 0

    # Saskaita visu izdevumu summas
    for exp in expenses:
        total += exp["amount"]

    return total


def sum_by_category(expenses):
    """
    Grupē izdevumus pa kategorijām un aprēķina summas.
    Atgriež dict: {kategorija: summa}
    """

    totals = {}

    for exp in expenses:
        category = exp["category"]

        # Ja kategorija vēl nav vārdnīcā, pievieno to
        if category not in totals:
            totals[category] = 0

        # Pieskaita summu attiecīgajai kategorijai
        totals[category] += exp["amount"]

    return totals


def get_available_months(expenses):
    """
    Atgriež unikālo mēnešu sarakstu formātā ["YYYY-MM", ...].
    """

    # Izmanto set, lai automātiski glabātu tikai unikālus mēnešus (bez dublikātiem)
    months = set()

    for exp in expenses:
        # Pārvērš datumu uz datetime objektu
        d = datetime.strptime(exp["date"], "%Y-%m-%d")

        # Izveido mēneša string formātā YYYY-MM
        month_str = f"{d.year}-{d.month:02d}"

        # Pievieno set (automātiski unikālas vērtības)
        months.add(month_str)

    # Sakārto rezultātu
    return sorted(months)