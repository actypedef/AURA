"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""
def add_tuple(nums, t):
    # Convert the tuple to a list and concatenate it with the original list
    nums += list(t)
    return nums

# Test the function with the provided test case
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
