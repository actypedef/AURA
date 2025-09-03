"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""
def check_Consecutive(nums):
    # Check if the sorted list of unique elements has no gaps between consecutive numbers
    return nums == list(range(min(nums), max(nums) + 1))

# Test the function with the provided test case
assert check_Consecutive([1, 2, 3, 4, 5]) == True
