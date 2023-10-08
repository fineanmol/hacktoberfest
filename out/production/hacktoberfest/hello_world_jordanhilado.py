# LANGUAGE: Python
# AUTHOR: Jordan Hilado
# GITHUB: https://github.com/jordanhilado

import itertools

print("".join([letter for letter in "hello world"])) 
print("".join([(lambda x:x.upper())(letter) for letter in "hello world"])) 
print("".join([(lambda x:x.upper())(letter) if letter in "hw" else letter for letter in "hello world"])) 
print("".join([(lambda x:x.upper())(letter) if letter in "hw" else letter for letter in itertools.chain("hello ","world")])) 
print("".join([(lambda x:x.upper())(letter) if letter in "hw" else letter for letters in zip("hlowrd","el ol.") for letter in letters ])) 