"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""
def empty_dit(dict_list):
    # Check if all dictionaries in the list are empty using a generator expression
    return all(not d for d in dict_list)

# Test the function with the provided test case
assert empty_dit([{},{},{}]) == True