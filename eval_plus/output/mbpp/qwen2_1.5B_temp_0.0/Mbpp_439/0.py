"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""
def multiple_to_single(numbers):
    """
    Join a list of multiple integers into a single integer.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The single integer formed by concatenating all integers in the list.
    """
    # Convert each integer in the list to a string and concatenate them
    concatenated_str = ''.join(map(str, numbers))
    # Convert the concatenated string back to an integer
    return int(concatenated_str)

# Test cases to verify the correctness of the solution
assert multiple_to_single([11, 33, 50]) == 113350
assert multiple_to_single([42, 67, 89]) == 426789
assert multiple_to_single([0, 0, 0]) == 0
assert multiple_to_single([-1, -2, -3]) == -123