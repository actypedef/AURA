"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""
def tetrahedral_number(n):
    """
    Calculate the nth tetrahedral number.

    Args:
    n (int): The position of the tetrahedral number in the sequence.

    Returns:
    int: The nth tetrahedral number.
    """
    return n * (n + 1) * (n + 2) // 6

# Test cases to verify the correctness of the solution
assert tetrahedral_number(5) == 35
assert tetrahedral_number(4) == 10
assert tetrahedral_number(1) == 1
assert tetrahedral_number(2) == 4
assert tetrahedral_number(3) == 10