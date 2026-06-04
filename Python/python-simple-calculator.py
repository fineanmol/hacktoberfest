#This is a simple python calculator made which can add, subtract, multiply and divide
#Enjoy having fun using it! :P

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

c=int(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))
d=0

if c==1:
    d=a+b

elif c==2:
    d=a-b

elif c==3:
    d=a*b

elif c==4:
    d=a/b

else:
    print("Error! You've entered the wrong command.")

print("The output is: ", d)