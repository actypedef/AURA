"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""
def divisor(n):
    # Initialize count to 0
    count = 0
    
    # Iterate through all numbers from 1 to n
    for i in range(1, n + 1):
        # If i is a divisor of n, increment the count
        if n % i == 0:
            count += 1
            
    return count

# Test the function with the provided test case
assert divisor(15) == 4
