import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a random password using the given options.
    
    :param length: Length of the password (default 12)
    :param use_uppercase: Include uppercase letters (default True)
    :param use_digits: Include digits (default True)
    :param use_special: Include special characters (default True)
    :return: Randomly generated password string
    """

    # Start with lowercase letters
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("No character sets selected for password generation.")

    # Ensure random selection
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


# Example usage
if __name__ == "__main__":
    print("Generated Password:", generate_password(length=16))
