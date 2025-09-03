"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""
def even_position(nums):
    # Iterate through the list using enumerate to get both index and value
    for i, x in enumerate(nums):
        # Check if the index is even and the number at that index is not even
        if i % 2 == 0 and x % 2 != 0:
            return False
    return True

# Test the function with the provided test case
assert even_position([3, 2, 1]) == False
