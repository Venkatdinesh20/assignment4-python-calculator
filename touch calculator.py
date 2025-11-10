"""
Simple Calculator Module
Assignment 4 - Git and JIRA Workflow Demo

This module demonstrates basic arithmetic operations for Git workflow and JIRA integration.
"""

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Test all calculator functions."""
    # Test addition
    print("Testing addition:")
    result = add(10, 5)
    print(f"10 + 5 = {result}")

    # Test subtraction
    print("\nTesting subtraction:")
    result = subtract(10, 5)
    print(f"10 - 5 = {result}")

    # Test multiplication
    print("\nTesting multiplication:")
    result = multiply(10, 5)
    print(f"10 * 5 = {result}")

    # Test division
    print("\nTesting division:")
    result = divide(10, 5)
    print(f"10 / 5 = {result}")

    # Test division by zero error handling
    print("\nTesting division by zero:")
    try:
        result = divide(10, 0)
    except ValueError as e:
        print(f"Error caught successfully: {e}")

if __name__ == "__main__":
    main()