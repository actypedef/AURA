"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
def test_duplicate(nums):
    # Convert the list to a set to remove duplicates
    unique_nums = set(nums)
    
    # Compare the length of the original list to the set
    if len(unique_nums) == len(nums):
        return False  # No duplicates found
    else:
        return True   # Duplicates found

# Test cases
assert test_duplicate([1, 2, 3, 4, 5]) == False
