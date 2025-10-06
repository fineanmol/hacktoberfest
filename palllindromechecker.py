# Palindrome_Checker.py
# This program checks if a given string or number is a palindrome

def is_palindrome(s):
    s = str(s).replace(" ", "").lower()  # Normalize: remove spaces, lowercase
    return s == s[::-1]

def main():
    user_input = input("Enter a string or number to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is NOT a palindrome.")

if __name__ == "__main__":
    main()

