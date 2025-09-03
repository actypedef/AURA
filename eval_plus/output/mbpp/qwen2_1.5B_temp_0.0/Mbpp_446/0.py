"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
def count_Occurrence(lst, tup):
    return sum(1 for item in lst if item in tup)

# Test cases
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3