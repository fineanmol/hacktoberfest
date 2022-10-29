import random

print(" *********************")
print("| Rock Paper Scissors |")
print(" *********************")

listCh = ["R", "P", "S"]

userScore = 0
computerScore = 0
i = 1

chance = int(input("How many times do you want to play (no. of chances)? "))

while i <= chance:
    computerCh = str(random.choice(listCh))

    userCh = input("Enter Rock, Paper, Scissors (key to press: R, P, S): ").upper()
    if userCh == computerCh:
        print("Tie!")

    elif userCh == "R":
        print("Computer Chooses: ", computerCh)
        if computerCh == "P":
            print("You lose! Paper covers Rock")
            computerScore += 1
        else:
            print("You win! Rock smashes Scissors")
            userScore += 1
    elif userCh == "P":
        print("Computer Chooses: ", computerCh)
        if computerCh == "S":
            print("You lose! Scissor cuts Paper")
            computerScore += 1
        else:
            print("You win! Paper covers Rock")
            userScore += 1

    elif userCh == "S":
        print("Computer Chooses: ", computerCh)
        if computerCh == "R":
            print("You lose! Rock smashes Scissors")
            computerScore += 1
        else:
            print("You win! Scissor cuts Paper")
            userScore += 1
    else:
        print(":(")

    print("\n\t******ScoreBoard******")
    print(f"\t You: {userScore} | Computer: {computerScore}")
    print("\t**********************")
    print(f"Game No:[{i}]")
    print("========================================================")

    i += 1

print("\n\n****** Game Over ******")
print("~~~~~~~~~~~~~~~~~~~~~~")
if userScore < computerScore:
    print("Sorry, You lost the game.")
    print("Computer Wins the game with score:", computerScore)
elif userScore == computerScore:
    print("Game tied")
else:
    print("Congratulaions, You won the Game. Your score:", userScore)
