import re

def is_flexible_palindrome(s):
    """
    Checks if a string is a palindrome by ignoring case, spaces, and punctuation.
    """
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]

# User input
text = input("Enter text or number: ")
if is_flexible_palindrome(text):
    print(f'"{text}" is a palindrome!')
else:
    print(f'"{text}" is not a palindrome!')

# Test cases
print("\nTest Cases:")
print("Racecar →", is_flexible_palindrome("Racecar"))  # True
print("A man, a plan, a canal: Panama →", is_flexible_palindrome("A man, a plan, a canal: Panama"))  # True
print("Hello →", is_flexible_palindrome("Hello"))  # False
print("12321 →", is_flexible_palindrome("12321"))  # True
print("Was it a car or a cat I saw? →", is_flexible_palindrome("Was it a car or a cat I saw?"))  # True
