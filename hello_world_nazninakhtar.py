"""
LANGUAGE: Python
ENV: Python 3.10
AUTHOR: Naznin Akhtar
GITHUB: https://github.com/nazninakhtar
"""

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return "Error: Division by zero" if b == 0 else a / b
    else:
        return "Invalid operator"

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))
    print("Result:", calculator(a, b, op))
