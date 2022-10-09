# Hello World Program
# Created by Amey Karan

import datetime

name = input("Enter your name: ")
finalName = ""
for word in name.split(" "):
    finalName += word[0].upper() + word[1:].lower()
    finalName += " "
finalName = finalName.rstrip(" ")
now = datetime.datetime.now()

print(now.strftime("%d %b 20%y %H:%M:%S"))
print("Hello, " + finalName + "!")
print("Have a lovely day.")
