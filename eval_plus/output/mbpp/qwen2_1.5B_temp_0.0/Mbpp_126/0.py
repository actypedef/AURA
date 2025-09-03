"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""
def sum_common_divisors(a, b):
    # Initialize sum of common divisors
    sum_div = 0
    
    # Iterate through all possible divisors from 1 to min(a, b)
    for i in range(1, min(a, b) + 1):
        # Check if both numbers are divisible by i
        if a % i == 0 and b % i == 0:
            # Add i to the sum of common divisors
            sum_div += i
            
    return sum_div

# Test cases to verify the correctness of the function
assert sum_common_divisors(10, 15) == 6
assert sum_common_divisors(28, 36) == 28
assert sum_common_divisors(49, 77) == 14
assert sum_common_divisors(100, 200) == 100