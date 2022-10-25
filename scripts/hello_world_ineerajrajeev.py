def rockPaperScissor():
    import random
    print("Welcome to Rock Paper Scissor Game")
    print("Enter your choice")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    choice = int(input())
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    elif choice == 3:
        choice_name = 'Scissor'
    else:
        print("Invalid Input")
        return
    print("Your choice is: " + choice_name)
    print("Now its computer turn...")
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'
    print("Computer choice is: " + comp_choice_name)
    print(choice_name + " V/s " + comp_choice_name)
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("Paper wins => ", end = "")
        result = "Paper"
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
    else:
        print("Scissor wins =>", end = "")
        result = "Scissor"
    if result == choice_name:
        print("<== You win ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    ans = input()
    if ans == 'n' or ans == 'N':
        exit()
    else:
        rockPaperScissor()