"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""
def remove_odd(numbers):
    """
    Remove odd numbers from a given list.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A new list containing only even numbers from the original list.
    """
    return [num for num in numbers if num % 2 == 0]

# Test cases to verify the correctness of the solution
assert remove_odd([1,2,3]) == [2]
assert remove_odd([4,5,6,7,8]) == [4,6,8]
assert remove_odd([11,13,15]) == []
assert remove_odd([]) == []
assert remove_odd([2,4,6,8,10]) == [2,4,6,8,10]