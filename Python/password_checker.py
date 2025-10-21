def contain_digits(password: str) -> bool:
    """
    Function to check if password contains digit or not .
    """
    for char in password:
        if char.isdigit():
            return True
    return False

def contain_special(password: str) -> bool:
    """
    Function to check for other characters except alphabets and digits.
    """
    for char in password:
        if not (char.isalpha() or char.isdigit()):
            return True
    return False

def validity_checker(password: str) -> bool:
    """
    Function to check whether given user input/password is valid or not as per given instructions
    """
    if len(password) < 6:
        return False
    if not (password[0].isalpha() and password[-1].isalpha()):
        return False
    if password.find(" ") != -1:
        return False
    if not contain_digits(password):
        return False
    return True

def strength(password: str) -> str:
    """
    Function to return strngth of password based on length and special characters usage.
    """
    if len(password) > 14:
        if contain_special(password):
            return "Strong"
        return "Medium"
    if len(password) > 10 and contain_special(password):
        return "Medium"
    return "Weak"

def check_password(password: str) -> str:
    """
    Function to check password using validity_checker function and strength function and return final verdict.
    """
    if validity_checker(password):
        return f"VALID PASSWORD! {strength(password)}"
    return "INVALID PASSWORD!"

def instructions():
    return """
        Welcome to PASSWORD CHECKER program

        Instructions for being a VALID password:
        1. Password should start and end with alphabets only.
        2. Password must contain digits.
        3. Spaces are not allowed in password.
        4. Special characters are allowed.
        5. Length of password must be greater than or equal to 6.
    """

if __name__ == "__main__":
    print(instructions())
    user = input("Enter a password to check: ")
    print(check_password(user))