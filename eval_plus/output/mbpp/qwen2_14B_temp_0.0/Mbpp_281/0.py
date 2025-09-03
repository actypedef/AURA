"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""
def all_unique(data):
    # Compare the length of the list with the length of the set created from the list
    return len(data) == len(set(data))

# Test the function with the provided test case
assert all_unique([1, 2, 3]) == True
