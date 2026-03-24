# =========================
# VALIDATION FUNCTIONS
# =========================

def is_valid_price(value):
    """
    Pārbauda vai ievadītā cena ir:
    - skaitlis (float)
    - lielāks par 0

    Atgriež:
    True  → derīga cena
    False → nederīga cena
    """
    try:
        price = float(value)
        return price > 0
    except ValueError:
        return False


def is_valid_qty(value):
    """
    Pārbauda vai daudzums ir:
    - vesels skaitlis (int)
    - lielāks par 0

    Atgriež:
    True  → derīgs daudzums
    False → nederīgs daudzums
    """
    try:
        qty = int(value)
        return qty > 0
    except ValueError:
        return False


# =========================
# CALCULATION FUNCTIONS
# =========================

def calc_line_total(item):
    """
    Aprēķina vienas preces kopējo summu:
    qty × price

    item piemērs:
    {
        "name": "Maize",
        "qty": 2,
        "price": 1.5
    }
    """
    return item["qty"] * item["price"]


def calc_grand_total(items):
    """
    Aprēķina visu produktu kopējo summu.

    items → saraksts ar produktiem
    """
    total = 0

    for item in items:
        total += calc_line_total(item)

    return total


def count_units(items):
    """
    Aprēķina kopējo vienību skaitu (qty summa).

    Piemērs:
    Maize ×2 + Piens ×3 = 5
    """
    total_qty = 0

    for item in items:
        total_qty += item["qty"]

    return total_qty