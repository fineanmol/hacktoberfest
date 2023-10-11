from sympy.crypto.crypto import AZ
from sympy.crypto.crypto import encipher_shift, decipher_shift

s = AZ(input("Enter Plaintext: "))
key = int(input("Enter Key: "))
print("Plain Text:", s)
print("Cipher Text:", encipher_shift(s, key))
print("Deciphered Text:", decipher_shift(encipher_shift(s, key), key))