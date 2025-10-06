"""Example: string_utils.py

Utility functions for strings used in exercises.
"""
from typing import List


def reverse_string(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    return sum(1 for ch in s.lower() if ch in 'aeiou')


if __name__ == "__main__":
    text = input("Enter text: ")
    print("Reversed:", reverse_string(text))
    print("Is palindrome:", is_palindrome(text))
    print("Vowels:", count_vowels(text))
