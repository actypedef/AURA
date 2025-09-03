"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""
def last_Digit_Factorial(n):
    # Initialize result
    fact = 1
    
    # If n is less than or equal to 4, return n directly
    if (n <= 4):
        return n
    
    # For n greater than 4, calculate the product of numbers from 5 to n
    for i in range(5, n + 1):
        fact *= i
    
    # Return the last digit of the factorial
    return fact % 10

# Test the function with the provided test case
assert last_Digit_Factorial(4) == 4