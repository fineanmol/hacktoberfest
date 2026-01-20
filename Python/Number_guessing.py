import random
print("\n\n----------------------------")
print("|   Number Guessing Game   |")
print("----------------------------")

a = int(input("\n\nEnter the lower limit : "))
b = int(input("\nEnter the upper limit : "))

num = random.randint(a, b)
#Number of guesses = number of hints = 3
#Let's try and randomize the hints

score = 100

# We'll use 2 lists, one to store hints and the other to store used hints
hints = list()
usedHints = list()

#Append hint1
hints.append(num*random.randint(2, 10))

i = 3

#Append hint2
while num%i != 0:
    i = i + 1
hints.append(i)

#Append hint3
hints.append(1000)

#No of chances = n
n = 1

while n!=4:
    guess = int(input("\nEnter your guess ({a} -> {b}) : ".format(a = a, b = b)))

    if(guess == num):
        print("Your guess was spot-on !\n\n")
        break
    if(n == 3):
        score = score - 30
        print("\nThe number was {num}".format(num = num))
        print("You have exhausted all your guesses. Better luck next time :)\n\n")
        break
    else:
        print("\n\n:( Try again")
        print("Here's a hint : ", end="")
        hintchoice = random.choice([i for i in hints if i not in usedHints])
        score = score - 30      
        if(hintchoice == 1000):
            if(guess > num):
                print("You guessed higher, try lowering it a bit\n\n")
            else:
                print("You guessed lower, try upping the stakes\n\n")
            usedHints.append(1000)
        else:
            if(hintchoice == hints[0]):
                print("{multiple} is a multiple of the number".format(multiple = hints[0]), end="\n\n")
                usedHints.append(hints[0])
            else:
                if(hintchoice == hints[1]):
                    print("The number is divisible by {divisible}".format(divisible = hints[1]), end="\n\n")
                    usedHints.append(hints[1])
    n = n + 1

print("Final Score : {score}".format(score = score))
