"""Example: calc.py

Provides a testable calculate() function and an interactive CLI guard.
"""
from typing import Union


def calculate(a: float, b: float, op: str) -> Union[float, str]:
    """Perform a calculation and return result or error string for invalid ops."""
    try:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                return "Error: divide by zero"
            return a / b
        if op == "**":
            return a ** b
        if op == "%":
            return a % b
        return "Error: unknown operation"
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    a = float(input("First number: "))
    b = float(input("Second number: "))
    op = input("Operation (+ - * / ** %): ")
    print(calculate(a, b, op))
