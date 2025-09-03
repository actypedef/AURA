"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
def test_duplicate(nums):
    # Convert the list to a set to remove duplicates
    nums_set = set(nums)
    
    # Compare the length of the set with the original list
    return len(nums) != len(nums_set)

# Test the function with the provided test case
assert test_duplicate([1, 2, 3, 4, 5]) == False
