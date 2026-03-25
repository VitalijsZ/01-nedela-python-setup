import json
import os

# =========================
# FILE PATH CONFIGURATION
# =========================

# Nosaka projekta direktoriju (kur atrodas šis fails)
BASE_DIR = os.path.dirname(__file__)

# Pilns ceļš līdz JSON failam, kur glabājas izdevumi
EXPENSES_FILE = os.path.join(BASE_DIR, "expenses.json")


# =========================
# STORAGE FUNCTIONS
# =========================

def load_expenses():
    """
    Nolasa expenses.json failu un atgriež izdevumu sarakstu.

    Ja fails neeksistē:
    - atgriež tukšu sarakstu []
    
    Atgriež:
        list: saraksts ar izdevumu objektiem
    """
    # Pārbauda vai fails eksistē
    if not os.path.exists(EXPENSES_FILE):
        return []

    # Atver failu lasīšanai un ielādē JSON datus
    with open(EXPENSES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_expenses(data):
    """
    Saglabā izdevumu sarakstu JSON failā.

    Parametri:
        data (list): saraksts ar izdevumu objektiem

    Funkcija pārraksta esošo failu ar jaunajiem datiem.
    """
    # Atver failu rakstīšanai un saglabā datus JSON formātā
    with open(EXPENSES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

