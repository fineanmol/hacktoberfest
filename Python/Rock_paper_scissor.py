'''
paper(1) beats rocks(0)
rocks(0) beats scissor(2) 
scissor(2) beats paper(1)
'''

scissors='''
    _____________
---'      _______)_______
                _________)_
          _________________)   
          (_______)
---'____  (____)   
'''

rock='''
   _____________
---'       _____)
           (_____)
           (_____)
           (____)
---'_______(___)
'''
paper='''
    _________
---'     ____)_____
            _______)
            ________)
            _______)
----'____________)
       
'''

game_images=[rock,paper,scissors]
import random


user_choice=int(input("what do you choose?  Type 0 for rock, 1 for paper or 2 for Scissors\n"))
if user_choice >=3 or user_choice < 0 :
    print("you entered an invalid number, you lose!")  
else :
    print(game_images[user_choice])

    computer_choice=random.randint(0,2)
    print(f"Computer chose:")
    print(game_images[computer_choice])

   
    if user_choice==0 and computer_choice==2:
        print("you Win!")
    elif computer_choice==0 and user_choice==2:
        print("you Lose")   
    elif computer_choice > user_choice:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice==user_choice:
        print("it's a draw")     
        