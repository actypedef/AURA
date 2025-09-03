"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""
def empty_dit(dicts):
    # Check if all dictionaries in the list are empty
    return all(not d for d in dicts)

# Test cases
assert empty_dit([{},{},{}])==True
assert empty_dit([{},{'a':1}])==False
assert empty_dit([])==True
assert empty_dit([{'a':1,'b':2},{'c':3}])==False