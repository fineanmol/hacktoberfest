a1 = b1 = 0

def game():
    a = input("Player 1 enter rock, paper or scissor: ").strip().lower()
    b = input("Player 2 enter rock, paper or scissor: ").strip().lower()
    global a1
    global b1

    if a == b:
        print("This round is draw")
        a1 += 1
        b1 += 1
    else:
        if a == "rock" and b == "scissor":
            a1 += 1
            print("Player 1 wins this round")

        elif a == "scissor" and b == "rock":
            b1 += 1
            print("Player 2 wins this round")

        elif a == "scissor" and b == "paper":
            a1 += 1
            print("Player 1 wins this round")

        elif a == "paper" and b == "rock":
            a1 += 1
            print("Player 1 wins this round")

        elif a == "paper" and b == "scissor":
            b1 += 1
            print("Player 2 wins this round")

for i in range(3):
    game()

if a1 == b1:
    print("It's an overall draw: Score: ", end="")
elif a1 > b1:
    print("Player 1 won: Score: ", end="")
else:
    print("Player 2 won: Score: ", end="")

print(a1, b1, end="-")
