"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
def count(lst):
    # Use the sum function to count True values in the list
    return sum(lst)

# Test the function with the provided test case
assert count([True, False, True]) == 2
