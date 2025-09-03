"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""
def sum_series(n):
    # Initialize the sum variable
    total_sum = 0
    
    # Loop through the series from 0 to n//2
    for i in range(n // 2 + 1):
        # Calculate the value of the current term in the series
        term = n - 2 * i
        
        # Add the term to the total sum
        total_sum += term
    
    return total_sum

# Test the function with the provided test case
assert sum_series(6) == 12