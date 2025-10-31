import random

class Bingo:
    def __init__(self):
        self.card = self.generate_card()
        self.called_numbers = []

    def generate_card(self):
        """Generate a Bingo card with random numbers."""
        card = []
        for i in range(5):
            if i == 0:
                numbers = random.sample(range(1, 16), 5)  # Column B (1-15)
            elif i == 1:
                numbers = random.sample(range(16, 31), 5)  # Column I (16-30)
            elif i == 2:
                numbers = random.sample(range(31, 46), 4)  # Column N (31-45) with 1 free space
                numbers.insert(2, "FREE")                # Insert free space
            elif i == 3:
                numbers = random.sample(range(46, 61), 5)  # Column G (46-60)
            elif i == 4:
                numbers = random.sample(range(61, 76), 5)  # Column O (61-75)
            card.append(numbers)
        return card

    def print_card(self):
        """Display the Bingo card."""
        print(" B   I   N   G   O")
        for i in range(5):
            for j in range(5):
                if j == 2 and i == 2:
                    print("FREE ", end="")
                else:
                    print(f"{self.card[j][i]:2} ", end="")
            print()  # New line after each row

    def draw_number(self):
        """Draw a random number for Bingo."""
        number = random.randint(1, 75)
        while number in self.called_numbers:
            number = random.randint(1, 75)
        self.called_numbers.append(number)
        return number

    def mark_number(self, number):
        """Mark the number on the Bingo card."""
        for i in range(5):
            for j in range(5):
                if self.card[j][i] == number:
                    self.card[j][i] = "X"  # Mark as crossed off

    def check_winner(self):
        """Check for a winner."""
        # Check rows and columns
        for i in range(5):
            if all(x == "X" for x in self.card[i]) or all(self.card[j][i] == "X" for j in range(5)):
                return True

        # Check diagonals
        if all(self.card[i][i] == "X" for i in range(5)) or all(self.card[i][4 - i] == "X" for i in range(5)):
            return True

        return False

if __name__ == "__main__":
    bingo_game = Bingo()
    bingo_game.print_card()

    while True:
        input("Press Enter to draw a number...")
        drawn_number = bingo_game.draw_number()
        print(f"Drawn number: {drawn_number}")
        bingo_game.mark_number(drawn_number)
        bingo_game.print_card()

        if bingo_game.check_winner():
            print("Bingo! You've won!")
            break
    print("Game Over")
