import json
import os

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "shopping.json")


def load_list():
    """Nolasa datus no JSON faila. Ja fails neeksistē, atgriež []."""
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_list(items):
    """Saglabā datus JSON failā."""
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)