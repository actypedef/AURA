"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""
def swap_List(lst):
    """
    Swap the first and last elements of a given list.

    Args:
    lst (list): The input list whose first and last elements are to be swapped.

    Returns:
    list: A new list with the first and last elements swapped.
    """
    if len(lst) > 0:
        # Swap the first and last elements
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Test cases to verify the correctness of the solution
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
assert swap_List([]) == []
assert swap_List([7]) == [7]
assert swap_List(['a', 'b', 'c']) == ['c', 'b', 'a']