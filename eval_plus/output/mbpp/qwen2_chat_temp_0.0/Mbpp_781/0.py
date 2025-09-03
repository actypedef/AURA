"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""
def count_divisors(n):
    # Initialize a counter for divisors
    divisor_count = 0
    
    # Loop through all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # If i is a divisor of n, increment the counter
        if n % i == 0:
            divisor_count += 1
    
    # Check if the number of divisors is even
    return divisor_count % 2 == 0

# Test the function with the provided test case
assert count_divisors(10) == False