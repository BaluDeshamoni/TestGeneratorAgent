# src/module.py

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def is_even(n):
    return n % 2 == 0

def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers do not have factorials.")
    if n == 0:
        return 1
    return n * factorial(n - 1)
