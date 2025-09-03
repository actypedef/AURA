"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""
def sumofFactors(n):
    # Initialize result
    res = 0
    
    # Loop through all possible factors
    for i in range(1, n + 1):
        if n % i == 0:  # Check if 'i' is a factor of 'n'
            if i % 2 == 0:  # Check if the factor is even
                res += i  # Add the even factor to the result
    
    return res

# Test the function with the provided test case
assert sumofFactors(18) == 26