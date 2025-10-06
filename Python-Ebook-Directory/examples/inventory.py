"""Example: inventory.py

Simple in-memory inventory with CSV persistence helpers.
"""
import csv
from typing import Dict, List


def add_item(inv: Dict[str, int], name: str, qty: int) -> None:
    inv[name] = inv.get(name, 0) + qty


def remove_item(inv: Dict[str, int], name: str) -> bool:
    if name in inv:
        del inv[name]
        return True
    return False


def save_inventory(inv: Dict[str, int], path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for name, qty in inv.items():
            writer.writerow([name, qty])


def load_inventory(path: str) -> Dict[str, int]:
    result: Dict[str, int] = {}
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                name, qty = row[0], int(row[1])
                result[name] = qty
    except FileNotFoundError:
        return {}
    return result


if __name__ == "__main__":
    inv = load_inventory("inventory.csv")
    print("Loaded", inv)
    add_item(inv, "apple", 5)
    save_inventory(inv, "inventory.csv")
    print("Saved.")
