#LANGUAGE: Python
#ENV: -
#AUTHOR: agusardi
#GITHUB: https://github.com/letdummy

author = "Agus"

def checkAuthor():
    if author == "Agus":
        return True

def hello_world():
    if checkAuthor():
        print('Hello, World!')
    else:
        print("Access Denied!!")

hello_world()