"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""
def neg_nos(nums):
    # Use list comprehension to filter out negative numbers
    result = [n for n in nums if n < 0]
    return result

# Test the function with the provided test case
assert neg_nos([-1, 4, 5, -6]) == [-1, -6]
