"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""
def last_Digit_Factorial(n):
    # Initialize result
    fact = 1
    
    # Compute factorial using modulo operation to keep only the last digit
    for i in range(2, n + 1):
        fact = (fact * i) % 10
    
    return fact

# Test the function with the provided test case
assert last_Digit_Factorial(4) == 4
