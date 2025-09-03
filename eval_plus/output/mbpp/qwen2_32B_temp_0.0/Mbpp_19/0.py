"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
def test_duplicate(arr):
    """
    This function checks if the given array contains any duplicate elements.
    """
    # Convert the array to a set to remove duplicates
    unique_elements = set(arr)
    
    # If the length of the set is less than the length of the array, there are duplicates
    return len(unique_elements) != len(arr)

# Test cases
assert test_duplicate([1, 2, 3, 4, 5]) == False
assert test_duplicate([1, 2, 3, 4, 5, 5]) == True
assert test_duplicate([1, 1, 1, 1, 1]) == True
assert test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
assert test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == True