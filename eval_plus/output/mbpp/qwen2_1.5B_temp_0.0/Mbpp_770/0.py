"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""
def odd_num_sum(n):
    """
    Calculate the sum of fourth power of first n odd natural numbers.

    Args:
    n (int): The number of initial odd natural numbers to consider.

    Returns:
    int: The sum of fourth power of first n odd natural numbers.
    """
    return sum([i**4 for i in range(1, 2*n, 2)])

# Test cases
assert odd_num_sum(2) == 82
assert odd_num_sum(3) == 985
assert odd_num_sum(4) == 1600
assert odd_num_sum(5) == 2725