"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""
def divisor(n):
    # Initialize count of divisors
    count = 0
    
    # Loop through all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # If i divides n without remainder, it is a divisor
        if n % i == 0:
            count += 1
            
    return count

# Test the function with the provided test case
assert divisor(15) == 4
