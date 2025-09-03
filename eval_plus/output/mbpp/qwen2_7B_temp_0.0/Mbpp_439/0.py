"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""
def multiple_to_single(nums):
    # Convert each number in the list to a string and concatenate them
    result = ''.join(str(num) for num in nums)
    # Convert the concatenated string back to an integer
    return int(result)

# Test the function with the provided test case
assert multiple_to_single([11, 33, 50]) == 113350