
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
def sort_array(array):
    # Check if the array is empty or contains only one element
    if len(array) <= 1:
        return array.copy()
    
    # Determine the sorting order based on the sum of the first and last elements
    if (array[0] + array[-1]) % 2 == 0:
        # Sort the array in descending order if the sum is even
        sorted_array = sorted(array, reverse=True)
    else:
        # Sort the array in ascending order if the sum is odd
        sorted_array = sorted(array)
    
    return sorted_array

# Test cases to verify the correctness of the function
assert sort_array([]) == [], "Test case for empty list failed"
assert sort_array([5]) == [5], "Test case for single-element list failed"
assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Test case for ascending order failed"
assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], "Test case for descending order failed"
