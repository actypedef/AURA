"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""
def last_Digit_Factorial(n):
    # If n is 0 or 1, the factorial is 1, so the last digit is 1
    if n == 0 or n == 1:
        return 1
    
    # Initialize the last digit variable
    last_digit = 1
    
    # Loop through numbers from 2 to n
    for i in range(2, n + 1):
        # Multiply the current last digit by i and update the last digit
        last_digit = (last_digit * (i % 10)) % 10
        
        # If at any point the last digit becomes 0, return 0
        if last_digit == 0:
            return 0
    
    return last_digit

# Test the function with the provided test case
assert last_Digit_Factorial(4) == 4
