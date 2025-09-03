"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""
def sum(n, m):
    # Initialize the sum of common divisors
    s = 0
    
    # Iterate through all possible divisors up to the minimum of n and m
    for i in range(1, min(n, m) + 1):
        # Check if both n and m are divisible by i
        if (n % i == 0 and m % i == 0):
            # Add the divisor to the sum
            s += i
    
    # Return the total sum of common divisors
    return s

# Test the function with the provided test case
assert sum(10, 15) == 6
