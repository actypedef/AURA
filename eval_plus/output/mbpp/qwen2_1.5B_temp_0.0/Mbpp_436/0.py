"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""
def neg_nos(lst):
    """
    Return a list of negative numbers from the given list.

    Args:
    lst (list): A list of integers.

    Returns:
    list: A list containing only the negative numbers from the input list.
    """
    # Use list comprehension to filter out negative numbers
    return [num for num in lst if num < 0]

# Test cases to verify the correctness of the function
assert neg_nos([-1,4,5,-6]) == [-1,-6]
assert neg_nos([1,2,3,4,5]) == []
assert neg_nos([-7,-8,-9]) == [-7,-8,-9]
assert neg_nos([]) == []