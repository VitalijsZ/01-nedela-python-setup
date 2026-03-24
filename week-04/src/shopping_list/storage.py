import json
import os

# Nosaka projekta direktoriju (kur atrodas šis fails)
BASE_DIR = os.path.dirname(__file__)

# Pilns ceļš līdz JSON failiem
SHOPPING_FILE = os.path.join(BASE_DIR, "shopping.json")
PRICES_FILE = os.path.join(BASE_DIR, "prices.json")


# =========================
# SHOPPING LIST OPERATIONS
# =========================

def load_list():
    """
    Nolasa shopping.json failu.
    Ja fails neeksistē → atgriež tukšu sarakstu.
    """
    if not os.path.exists(SHOPPING_FILE):
        return []

    with open(SHOPPING_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_list(items):
    """
    Saglabā iepirkumu sarakstu JSON failā.
    items → saraksts ar produktiem
    """
    with open(SHOPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)


# =========================
# PRICES DATABASE OPERATIONS
# =========================

def load_prices():
    """
    Nolasa prices.json failu.
    Ja fails neeksistē → atgriež tukšu dict.
    """
    if not os.path.exists(PRICES_FILE):
        return {}

    with open(PRICES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_prices(prices):
    """
    Saglabā cenu vārdnīcu prices.json failā.
    prices → dict formāts { "Maize": 1.2 }
    """
    with open(PRICES_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)


def get_price(name):
    """
    Atgriež produkta cenu no prices.json.
    Ja produkts nav atrasts → None
    """
    prices = load_prices()
    return prices.get(name)


def set_price(name, price):
    """
    Pievieno vai atjaunina produkta cenu prices.json.
    """
    prices = load_prices()
    prices[name] = price
    save_prices(prices)