"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""
import math

def count_divisors(n):
    count = 0
    # Iterate from 1 to the square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # If divisors are equal, count only once
            if n // i == i:
                count += 1
            else:
                # Count both divisors
                count += 2
    # Check if the count of divisors is even
    return count % 2 == 0

# Test the function with the provided test case
assert count_divisors(10)
