def is_valid_price(value):
    """Pārbauda vai cena ir pozitīvs skaitlis."""
    try:
        price = float(value)
        return price > 0
    except ValueError:
        return False


def is_valid_qty(value):
    """Pārbauda vai daudzums ir pozitīvs vesels skaitlis."""
    try:
        qty = int(value)
        return qty > 0
    except ValueError:
        return False


def calc_line_total(item):
    """Aprēķina vienas rindas summu (qty × price)."""
    return item["qty"] * item["price"]


def calc_grand_total(items):
    """Aprēķina kopējo summu visiem produktiem."""
    total = 0
    for item in items:
        total += calc_line_total(item)
    return total


def count_units(items):
    """Aprēķina kopējo vienību skaitu."""
    total_qty = 0
    for item in items:
        total_qty += item["qty"]
    return total_qty