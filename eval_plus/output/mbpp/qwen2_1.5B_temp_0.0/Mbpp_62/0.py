"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""
def smallest_num(lst):
    return min(lst)

# Test cases
assert smallest_num([10, 20, 1, 45, 99]) == 1
assert smallest_num([-5, -3, -7, -1]) == -7
assert smallest_num([0, 0, 0, 0]) == 0
assert smallest_num([100, 200, 300, 400]) == 100