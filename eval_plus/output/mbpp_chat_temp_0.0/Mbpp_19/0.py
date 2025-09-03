"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
def test_duplicate(nums):
    # Convert the list to a set to remove duplicates and compare lengths
    return len(set(nums)) != len(nums)

# Test the function with the provided test case
assert test_duplicate([1, 2, 3, 4, 5]) == False
