import random

number = random.randint(1, 100)
attempts = 0
guess = None

print("🎯 Guess the Number (1 to 100)!")

while guess != number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"🎉 You got it in {attempts} tries!")
    except ValueError:
        print("⚠️ Please enter a valid number.")
