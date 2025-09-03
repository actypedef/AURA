"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
def sum_digits(n):
    # Initialize the sum to 0
    s = 0
    
    # Loop until n becomes 0
    while n > 0:
        # Add the last digit of n to s
        s += n % 10
        # Remove the last digit from n
        n //= 10
    
    # Return the computed sum
    return s

# Test the function with the provided test case
assert sum_digits(345) == 12
