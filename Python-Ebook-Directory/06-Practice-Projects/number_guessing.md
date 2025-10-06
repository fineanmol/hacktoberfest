# Number Guessing Game

A small CLI game where the player guesses a randomly chosen number.

```python
import random

secret = random.randint(1, 20)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    tries += 1
    if guess == secret:
        print(f"Correct! You guessed it in {tries} tries.")
        break
    elif guess < secret:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
```

Enhancements: add a high score file, difficulty levels, or limited attempts.
