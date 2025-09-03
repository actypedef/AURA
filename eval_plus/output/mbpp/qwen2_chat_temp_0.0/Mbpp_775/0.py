"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""
def odd_position(nums):
    # Iterate through the list using enumerate to get both index and value
    for i, x in enumerate(nums):
        # Check if the index is odd and the number at that index is not odd
        if i % 2 != 0 and x % 2 == 0:
            return False
    return True

# Test the function with the provided test case
assert odd_position([2, 1, 4, 3, 6, 7, 6, 3]) == True