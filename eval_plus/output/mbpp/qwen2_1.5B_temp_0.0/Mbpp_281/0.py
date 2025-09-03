"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""
def all_unique(lst):
    return len(set(lst)) == len(lst)

# Test cases
assert all_unique([1,2,3]) == True
assert all_unique([1,2,2]) == False
assert all_unique([]) == True
assert all_unique(['a', 'b', 'c']) == True
assert all_unique(['a', 'a', 'b']) == False