# This function performs additiion
def add(a, b):
   return a + b
# This function performs subtraction
def subtract(a, b):
   return a - b
# This function performs multiplication
def multiply(a, b):
   return a * b
# This function performs division
def divide(a, b):
    return a / b


print("Select an operation.")
print("+")
print("-")
print("*")
print("/")
# User input
choice = input("Enter operator to use:")
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
if choice == '+':
   print(A,"+",B,"=", add(A,B))
elif choice == '-':
   print(A,"-",B,"=", subtract(A,B))
elif choice == '*':
   print(A,"*",B,"=", multiply(A,B))
elif choice == '/':
      if B==0:
         print("Divided by zero Error")
      print(A,"/",B,"=", divide(A,B))
else:
    print("Invalid input")