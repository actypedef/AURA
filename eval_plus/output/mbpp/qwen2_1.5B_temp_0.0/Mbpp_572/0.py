"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""
def two_unique_nums(nums):
    # Convert list to set to remove duplicates
    unique_nums = set(nums)
    # Convert set back to list
    return list(unique_nums)

# Test the function
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]