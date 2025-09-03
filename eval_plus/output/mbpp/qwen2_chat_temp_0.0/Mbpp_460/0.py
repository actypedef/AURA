"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""
def Extract(lst):
    # Use list comprehension to iterate through each sublist and extract the first element
    return [sublist[0] for sublist in lst]

# Test the function with the provided test case
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
