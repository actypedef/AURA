"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""
def count_divisors(n):
    # Initialize a counter for divisors
    c = 0
    
    # Loop through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Increment the counter if i is a divisor
            c += 1
    
    # Return True if the count of divisors is even, False otherwise
    return c % 2 == 0

# Test the function with the provided test case
assert count_divisors(10) == True
