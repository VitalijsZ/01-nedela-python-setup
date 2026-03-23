def is_valid_price(value):
    """Pārbauda vai cena ir pozitīvs skaitlis."""
    try:
        price = float(value)
        return price > 0
    except ValueError:
        return False