"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""
def multiple_to_single(nums):
    # Convert each integer in the list to a string and concatenate them
    result = int(''.join(str(i) for i in nums))
    return result

# Test the function with the provided test case
assert multiple_to_single([11, 33, 50]) == 113350
