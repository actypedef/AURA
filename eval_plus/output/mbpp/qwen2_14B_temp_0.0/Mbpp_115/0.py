"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""
def empty_dit(list1):
    # Check if all dictionaries in the list are empty
    all_empty = all(not d for d in list1)
    return all_empty

# Test the function with the provided test case
assert empty_dit([{},{},{}]) == True
