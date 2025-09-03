"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
def test_duplicate(arr):
    # Convert the list to a set to remove duplicates
    unique_arr = set(arr)
    # Check if the length of the original array is equal to the length of the set
    return len(arr) != len(unique_arr)

# Test the function with provided data points
assert test_duplicate(([1,2,3,4,5])) == False