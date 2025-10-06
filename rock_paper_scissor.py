
a1=b1=0
def game():
    a=input("Player 1 enter rock,paper or scissor: ")
    b=input("Player 2 enter rock,paper or scissor: ")
    global a1
    global b1
    if a==b:
        print("This round is draw")
        a1+=1
        b1+=1
    else:
        if a=="rock" and (b=="scissor" or b=="paper"):
            a1+=1
            print("Player 1 wins this round")

        elif a=="scissor" and b=="rock":
            b1+=1
            print("Player 2 wins this round")
        elif a=="scissor" and b=="paper":
            a1+=1
            print("Player 1 wins this round")
        elif a=="paper" and (b=="rock" or b=="scissor"):
            b1+=1
            print("Player 2 wins this round")
game()
game()
game()
if a1==b1:
    print("It's an overall draw: Score: ",end="")

elif a1>b1:
    print("Player 1 won: Score: ",end="")
else:
    print("Player 2 won: Score: ",end="")
print(a1,b1,end="-")