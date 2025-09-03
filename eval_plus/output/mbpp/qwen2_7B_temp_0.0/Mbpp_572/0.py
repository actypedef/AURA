"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""
def two_unique_nums(nums):
    # Use set to remove duplicates and then convert back to list
    return list(set(nums))

# Test the function with the provided test case
assert two_unique_nums([1, 2, 3, 2, 3, 4, 5]) == [1, 4, 5]
