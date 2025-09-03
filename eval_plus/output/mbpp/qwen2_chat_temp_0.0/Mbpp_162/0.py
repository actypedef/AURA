"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""
def sum_series(n):
    # Initialize the result variable to store the sum
    res = 0
    
    # Loop through the range from 0 to n//2 (inclusive)
    for i in range(n // 2 + 1):
        # Add the value of n - 2*i to the result
        res += n - 2 * i
    
    # Return the computed sum
    return res

# Test the function with the provided test case
assert sum_series(6) == 12
