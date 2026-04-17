import math
import re

def parse_number(token):
    """
    Parse a string token into int, float, or complex number.
    """
    try:
        if 'j' in token:
            return complex(token)
        elif '.' in token:
            return float(token)
        else:
            return int(token)
    except:
        raise ValueError(f"Invalid number: {token}")


def calculate(a, b, operator):
    """
    Perform basic arithmetic operations.
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '%':
        # Modulo is not supported for complex numbers
        if isinstance(a, complex) or isinstance(b, complex):
            return "Modulo not supported for complex numbers"
        return a % b
    else:
        raise ValueError("Unsupported operator")


def factorial(n):
    """
    Calculate factorial of a non-negative integer.
    """
    if isinstance(n, complex):
        return "Factorial not supported for complex numbers"
    if isinstance(n, float):
        return "Factorial only supports integers"
    if n < 0:
        return "Factorial not defined for negative numbers"
    return math.factorial(n)


def evaluate(expression):
    """
    Evaluate a simple mathematical expression.
    Supports:
    - Binary operations: +, -, *, /, %
    - Factorial: n!
    """
    # Remove all spaces from input
    expression = expression.replace(" ", "")

    # Handle factorial (e.g., 5!)
    if expression.endswith('!'):
        num_part = expression[:-1]
        n = parse_number(num_part)
        return factorial(n)

    # Match binary expression: a operator b
    match = re.match(r"(.+?)([\+\-\*/%])(.+)", expression)
    if match:
        left, operator, right = match.groups()
        a = parse_number(left)
        b = parse_number(right)
        return calculate(a, b, operator)

    return "Invalid expression"


# ===== Interactive calculator =====
if __name__ == "__main__":
    print("Simple Calculator (type 'exit' to quit)")
    while True:
        expr = input(">>> ")
        if expr.lower() == "exit":
            break
        try:
            result = evaluate(expr)
            print(result)
        except Exception as e:
            print("Error:", e)