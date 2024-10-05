#LANGUAGE: Python
#ENV: Python
#AUTHOR: Shivakumar Mazhuvan
#GITHUB: https://github.com/smazhuvan

import time
import random

# Fun 'typing' effect function
def typing_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.03, 0.1))  # Random typing speed
    print()

# Creative "Hello, World!" with ASCII art
def hello_world_art():
    art = """
  _   _      _ _         __        __         _     _ 
 | | | |    | | |        \ \      / /        | |   | |
 | |_| | ___| | | ___     \ \ /\ / /__  _   _| |__ | |
 |  _  |/ _ \ | |/ _ \     \ V  V / _ \| | | | '_ \| |
 | | | |  __/ | | (_) |     \_/\_/ (_) | |_| | |_) |_|
 |_| |_|\___|_|_|\___( )         (_)   \__,_|_.__/(_)
                    |/                                
    """
    typing_effect(art)

# Fun function to display basic info
def display_info():
    name = "Shivakumar Mazhuvan"
    age = 29
    hobby = "Coding"
    
    info = f"""
    👋 Hello, World!
    My name is {name} 🌍
    I'm {age} years old 🎂
    I love {hobby} 💻
    """
    typing_effect(info)

# Call functions
hello_world_art()
display_info()
