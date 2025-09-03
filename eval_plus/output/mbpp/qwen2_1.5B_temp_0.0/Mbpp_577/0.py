"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""
def last_Digit_Factorial(n):
    # Initialize the result variable to 1 (since 1! = 1)
    result = 1
    
    # Loop from 2 to n
    for i in range(2, n + 1):
        # Multiply the current result by the current number
        result *= i
        
        # Get the last digit of the result
        last_digit = result % 10
    
    return last_digit

# Test cases to verify the correctness of the function
assert last_Digit_Factorial(4) == 4
assert last_Digit_Factorial(5) == 0
assert last_Digit_Factorial(6) == 6
assert last_Digit_Factorial(7) == 4
assert last_Digit_Factorial(8) == 2
assert last_Digit_Factorial(9) == 0
assert last_Digit_Factorial(10) == 0