"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""
def find_star_num(n):
    """
    Calculate the n-th star number.
    
    Args:
    n (int): The position of the star number in the sequence.
    
    Returns:
    int: The n-th star number.
    """
    return n * (4 * n - 3)

# Test cases to verify the correctness of the solution
assert find_star_num(1) == 1
assert find_star_num(2) == 5
assert find_star_num(3) == 37
assert find_star_num(4) == 81
assert find_star_num(5) == 165