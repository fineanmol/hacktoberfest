"""Example: guess_game.py

Number guessing game packaged so tests can import and check helper logic.
"""
import random
from typing import Tuple


def pick_secret(low: int = 1, high: int = 20) -> int:
    return random.randint(low, high)


def check_guess(secret: int, guess: int) -> Tuple[bool, str]:
    if guess == secret:
        return True, "correct"
    if guess < secret:
        return False, "low"
    return False, "high"


if __name__ == "__main__":
    secret = pick_secret()
    while True:
        guess = int(input("Guess a number: "))
        ok, hint = check_guess(secret, guess)
        if ok:
            print("Correct")
            break
        print(hint)
