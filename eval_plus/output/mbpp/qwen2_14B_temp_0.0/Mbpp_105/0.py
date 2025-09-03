"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
def count(lst):
    # Count the number of True boolean values in the list
    return lst.count(True)

# Test the function with the provided test case
assert count([True, False, True]) == 2
