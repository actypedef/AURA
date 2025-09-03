"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""
def sum_div(n):
    # Initialize the sum of divisors to 0
    s = 0
    
    # Loop through numbers from 1 to n-1 to find divisors
    for i in range(1, n):
        if n % i == 0:  # Check if i is a divisor of n
            s += i  # Add the divisor to the sum
    
    return s

# Test the function with the provided test case
assert sum_div(8) == 7