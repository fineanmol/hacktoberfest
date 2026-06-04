def create_cipher(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = dict(zip(alphabet, key))
    return cipher

def encrypt(plain_text, cipher):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            uppercase_char = char.upper()
            if uppercase_char in cipher:
                encrypted_char = cipher[uppercase_char]
                if char.islower():
                    encrypted_char = encrypted_char.lower()
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, cipher):
    decryption_key = {v: k for k, v in cipher.items()}
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            uppercase_char = char.upper()
            if uppercase_char in decryption_key:
                decrypted_char = decryption_key[uppercase_char]
                if char.islower():
                    decrypted_char = decrypted_char.lower()
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
key = "XZVTPONMLKJIHGFEDCBA"
text = "Hello, World!"

cipher = create_cipher(key)
encrypted_text = encrypt(text, cipher)
decrypted_text = decrypt(encrypted_text, cipher)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
