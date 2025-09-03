"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""
def sum(n1, n2):
    # Initialize the sum of common divisors to 0
    sum = 0
    
    # Iterate through all possible divisors up to the minimum of n1 and n2
    for i in range(1, min(n1, n2) + 1):
        # Check if both n1 and n2 are divisible by i
        if (n1 % i == 0) and (n2 % i == 0):
            # Add the divisor to the sum
            sum += i
            
    return sum

# Test the function with the provided test case
assert sum(10, 15) == 6