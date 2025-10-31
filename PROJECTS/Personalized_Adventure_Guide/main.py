#' '
#" "
#''' '''
#""" """ 
name=input("Hello User: Please Enter your name \n")

print("Welcome to the class 3A "+name)

message='Hello '+name+' Welcome to Personalized Adventure Guide'
print(message)

message='Hello {var} Welcome to Personalized Adventure Guide'.format(var=name)
print(message)

print(f"Hello {name.title()}, Welcome to Personalized Adventure Guide")

"""
take the input from the user
"mountain" or 
"beach"
"""

destination=input("Where do you want to go \n").strip().lower()
if destination == "mountain":
    print("You are going to the mountain")
elif destination == "beach":
    print("You are going to the beach")
else:
    print("Enter the correct choice")

"""Take budget and number of days from the user
if budget:
    >=500 -> Luxury
    200<= budget <500 -> good
    0<budget<200 -> budget friendly
"""         
budget=int(input("Enter the budget : "))
if budget >=500:
    print("Luxury")
elif  budget>=200:
    print("Good")
elif budget >0:
    print("Budget friendly")
else:
    print("Invalid budget")

#days
days=int(input("Enter the number of days \n"))
totalCost=days*budget

print(f"""
days = {days} \n
budget = {budget} \n
total cost = {totalCost}""")