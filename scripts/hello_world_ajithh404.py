LANGUAGE: Python

AUTHOR: Ajith

GITHUB: https://github.com/ajithh404

DESCRIPTION: Instead of printing the whole message at once, this script uses a Python Generator to stream out "Hello, World!" one character at a time. 
It’s like a tiny, efficient message pipeline!

def hello_generator():
    '''Generates the 'Hello, World!' string character by character'''
    message = "Hello, World!"
    for char in message:
        yield char
      
'''Join the yielded characters and print'''      
print("".join(hello_generator()))
