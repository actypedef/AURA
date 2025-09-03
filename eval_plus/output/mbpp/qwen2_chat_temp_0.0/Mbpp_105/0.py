"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
def count(lst):
    # Count the number of True values in the list using a generator expression
    return sum(1 for x in lst if x)

# Test the function with the provided test case
assert count([True, False, True]) == 2
