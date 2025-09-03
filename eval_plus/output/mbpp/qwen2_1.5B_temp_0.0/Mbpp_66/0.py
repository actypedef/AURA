"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""
def pos_count(lst):
    return sum(1 for x in lst if x > 0)

# Test cases
assert pos_count([1,-2,3,-4]) == 2
assert pos_count([-1, -2, -3, -4]) == 0
assert pos_count([0, 1, 2, 3, 4]) == 5
assert pos_count([]) == 0