"""
Write a function to filter odd numbers.
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
"""
def filter_odd_numbers(numbers):
    """
    Filter out even numbers from a list of integers.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A list containing only the odd numbers from the input list.
    """
    return [num for num in numbers if num % 2 != 0]

# Test cases to verify the correctness of the solution
assert filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
assert filter_odd_numbers([11, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == [11, 33, 55, 77, 99]
assert filter_odd_numbers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-1, -3, -5, -7, -9]
assert filter_odd_numbers([]) == []
assert filter_odd_numbers([2, 4, 6, 8, 10]) == []