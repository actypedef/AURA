"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""
# Define a function to check if all dictionaries in a list are empty
def empty_dit(dict_list):
    # Use the all() function to check if all dictionaries in the list are empty
    return all(not d for d in dict_list)

# Test the function with the provided test case
assert empty_dit([{},{},{}]) == True
