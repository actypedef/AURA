"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""
def pair_wise(nums):
    # Create a list of tuples containing consecutive pairs using zip
    result = list(zip(nums[:-1], nums[1:]))
    return result

# Test the function with the provided test case
assert pair_wise([1, 1, 2, 3, 3, 4, 4, 5]) == [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
