"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""
def count_divisors(n):
    # Initialize divisor count to 0
    count = 0
    
    # Loop through all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # If 'i' divides 'n' without leaving a remainder, it's a divisor
        if n % i == 0:
            count += 1
            
    # Check if the count of divisors is even
    return count % 2 == 0

# Test cases
assert count_divisors(10) == True
assert count_divisors(15) == False
assert count_divisors(16) == True
assert count_divisors(17) == False