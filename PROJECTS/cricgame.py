import random

def userBatFirst():
    userScoreSheet = []
    compBowl = random.randint(1, 6)
    userShot = None
    noOfBalls = 0
    global userscore
    userscore = 0
    while userShot != compBowl and noOfBalls < 10:     
        try:
            userShot = int(input('Enter to Bat (1-6): '))
            if userShot < 1 or userShot > 6:
                raise ValueError("Shot must be between 1 and 6")
            userScoreSheet.append(userShot)
            noOfBalls += 1
        except ValueError as e:
            print(e)
    print("your innings over!")
    # print(userScoreSheet)
    for elem in userScoreSheet:
        userscore += elem
    print("you scored",userscore)


def userballfirst():
    compScoreSheet = []
    userBowl = None
    compShot = 0
    noOfBalls = 0
    global compscore
    compscore = 0
    while compShot != userBowl and noOfBalls < 10:
        try:
            userBowl = int(input('Enter to bowl (1-6): '))
            if userBowl < 1 or userBowl > 6:
                raise ValueError("Bowl must be between 1 and 6")
            compShot = random.randint(1, 6)
            compScoreSheet.append(compShot)
            noOfBalls += 1
        except ValueError as e:
            print(e)
    #print(compScoreSheet)
    for elem in compScoreSheet:
        compscore += elem
    print("computer innings over!")
    print("comp scored",compscore)
 
def checkWinner():
    if compscore < userscore:
        print("You won")
    elif compscore == userscore:
        print("It's a tie")
    else:
        print("Computer won")
while True:
 try:
     tossCoinChoice = int(input('Type 1 for heads or type 2 for tails: '))
     if tossCoinChoice not in [1, 2]:
        raise ValueError("Toss choice must be 1 or 2")
     
     tossResult = random.randint(1, 2)
    
     if tossCoinChoice == tossResult:
        print('You won the toss')
        tossWinChoice = input('Press 1 for batting first, press 2 for bowling: ')
        if tossWinChoice == '1':
            userBatFirst()
            userballfirst()
        else:
            userballfirst()
            userBatFirst()
     else:
        print('You lost the toss') 
        print('Computer chose to bat first')
        userballfirst()
        userBatFirst()
     checkWinner()

     play_again = input('Do you want to play again? (yes/no): ')
     if play_again.lower() != 'yes':
        break

 except ValueError as e:
    print(e)
