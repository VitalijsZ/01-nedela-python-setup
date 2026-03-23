import json
import os

FILE_PATH = "shopping_list/shopping.json"


def load_data():
    """Nolasa datus no JSON faila. Ja fails neeksistē, atgriež []."""
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    """Saglabā datus JSON failā."""
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)