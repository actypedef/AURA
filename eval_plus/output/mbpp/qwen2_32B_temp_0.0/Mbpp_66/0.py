"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""
def pos_count(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    return count

assert pos_count([1, -2, 3, -4]) == 2
assert pos_count([1, 2, 3, 4]) == 4
assert pos_count([-1, -2, -3, -4]) == 0
assert pos_count([]) == 0