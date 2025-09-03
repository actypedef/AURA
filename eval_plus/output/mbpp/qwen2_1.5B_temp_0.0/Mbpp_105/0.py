"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
def count(lst):
    return lst.count(True)

# Test cases
assert count([True,False,True]) == 2
assert count([False,False,False]) == 0
assert count([True,True,True,True]) == 4
assert count([]) == 0