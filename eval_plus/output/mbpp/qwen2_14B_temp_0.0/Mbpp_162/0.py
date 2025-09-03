"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""
def sum_series(n):
    # Initialize the sum to 0
    sm = 0
    
    # Iterate from 0 to n // 2
    for i in range(n // 2 + 1):
        # Add the current term (n - 2 * i) to the sum
        sm += (n - 2 * i)
    
    return sm

# Test the function with the provided test case
assert sum_series(6) == 12
