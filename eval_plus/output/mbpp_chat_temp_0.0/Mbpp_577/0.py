"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""
def last_Digit_Factorial(n):
    # Initialize result variable
    res = 1
    
    # Loop through numbers from 2 to n
    for i in range(2, n + 1):
        # Multiply result with the last digit of current number
        res = (res * (i % 10)) % 10
    
    # Return the last digit of the factorial
    return res

# Test the function with the provided test case
assert last_Digit_Factorial(4) == 4