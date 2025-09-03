"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""
def sum_series(n):
    """
    Calculate the sum of (n - 2*i) from i=0 to n // 2.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The calculated sum.
    """
    total_sum = 0
    for i in range(n // 2 + 1):
        total_sum += (n - 2 * i)
    return total_sum

# Test cases to verify the correctness of the solution
assert sum_series(6) == 12
assert sum_series(8) == 24
assert sum_series(10) == 30