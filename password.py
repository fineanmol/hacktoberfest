import random
import string

def generate_password(length=12):
    # Define the character sets to use for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?"
    
    # Ensure that the password length is at least 12 characters
    if length < 12:
        length = 12
    
    # Create a pool of characters to choose from
    password_characters = (lowercase_letters +
                          uppercase_letters +
                          digits +
                          special_characters)
    
    # Generate a random password
    password = ''.join(random.choice(password_characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    if password_length < 12:
        print("A strong password should be at least 12 characters long.")
    else:
        strong_password = generate_password(password_length)
        print("Your strong password is:", strong_password)
