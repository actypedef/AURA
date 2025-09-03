"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
def sum_digits(n):
    # Initialize a variable to store the sum of digits
    s = 0
    
    # Loop through each digit in the number
    while n > 0:
        # Add the last digit to the sum
        s += n % 10
        # Remove the last digit from the number
        n //= 10
    
    # Return the total sum of digits
    return s

# Test the function with the provided test case
assert sum_digits(345) == 12
