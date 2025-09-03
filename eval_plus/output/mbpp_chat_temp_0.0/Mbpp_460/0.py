"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""
def Extract(lst):
    # Use list comprehension to iterate through each sublist in the input list 'lst'
    # For each sublist, extract the first element using indexing (sublist[0])
    return [sublist[0] for sublist in lst]

# Test the function with the provided test case
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
