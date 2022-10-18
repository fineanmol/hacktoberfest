# LANGUAGE: Python
# ENV: Python3
# AUTHOR: Raunak Saigal
# GITHUB: https://github.com/raunaksaigal

from random import randint
world = ["Hello World", "Heya!", "Hello Fellas"]
t = True

while t:
    q = randint(0,2)
    i = input("Enter to continue, q to quit")
    if i == '':
        print(world[q])
    else:
        break