"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""
def divisor(n):
    # Initialize a counter for divisors
    count = 0
    
    # Loop through all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Increment the counter if i is a divisor
            count += 1
    
    # Return the total count of divisors
    return count

# Test the function with the provided test case
assert divisor(15) == 4
