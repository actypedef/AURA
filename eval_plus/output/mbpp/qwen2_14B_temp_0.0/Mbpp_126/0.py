"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""
def sum(a, b):
    # Initialize sum of common divisors to 0
    total = 0
    
    # Iterate through all numbers from 1 to the minimum of a and b
    for i in range(1, min(a, b) + 1):
        # Check if i is a divisor of both a and b
        if a % i == 0 and b % i == 0:
            # Add i to the sum if it is a common divisor
            total += i
    
    return total

# Test the function with the provided test case
assert sum(10, 15) == 6
