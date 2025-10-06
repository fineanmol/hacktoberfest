"""Example: profile_save

Provides functions to format and parse profile lines. Interactive saving is under __main__.
"""
from datetime import datetime
from typing import Dict


def format_profile(name: str, age: int, city: str) -> str:
    """Return a single-line representation for storage."""
    ts = datetime.utcnow().isoformat()
    return f"{ts},{name},{age},{city}\n"


def parse_profile(line: str) -> Dict[str, str]:
    """Parse a stored line and return a dict."""
    ts, name, age, city = line.strip().split(",")
    return {"timestamp": ts, "name": name, "age": age, "city": city}


if __name__ == "__main__":
    name = input("Name: ")
    age = input("Age: ")
    city = input("City: ")
    line = format_profile(name, int(age), city)
    with open("profiles.txt", "a", encoding="utf-8") as f:
        f.write(line)
    print("Saved.")
