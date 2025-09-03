
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
def sort_array(arr):
    """
    Sorts an array of non-negative integers according to the number of ones in their binary representation,
    then by their decimal values if the number of ones is the same.
    
    :param arr: List of non-negative integers
    :return: Sorted list of integers
    
    Examples:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """
    # Convert each integer to a tuple containing the count of ones in its binary representation and the integer itself
    binary_ones = [(bin(x).count('1'), x) for x in arr]
    # Sort the tuples first by the count of ones, then by the integer value
    sorted_arr = sorted(binary_ones)
    # Extract the sorted integers from the tuples
    return [x[1] for x in sorted_arr]

# Test cases