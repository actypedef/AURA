"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""
def first_odd(numbers):
    """
    Find the first odd number in a given list of numbers.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The first odd number in the list.
    """
    for num in numbers:
        if num % 2 != 0:
            return num

# Test cases
assert first_odd([1,3,5]) == 1
assert first_odd([2,4,6]) == None
assert first_odd([10,22,34,56]) == 5
assert first_odd([-1, -3, -5]) == -1
assert first_odd([]) == None