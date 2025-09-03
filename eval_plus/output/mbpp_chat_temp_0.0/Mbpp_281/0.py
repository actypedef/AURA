"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""
def all_unique(data):
    # Convert the list to a set to remove duplicates and compare its length to the original list
    return len(set(data)) == len(data)

# Test the function with the provided test case
assert all_unique([1, 2, 3]) == True
