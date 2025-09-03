"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""
def empty_list(n):
    """
    Create a list of N empty dictionaries.

    Args:
    n (int): The number of empty dictionaries to create.

    Returns:
    list: A list containing N empty dictionaries.
    """
    return [{}] * n

# Test cases to verify the correctness of the function
assert empty_list(5) == [{}, {}, {}, {}, {}]
