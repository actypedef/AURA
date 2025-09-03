"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""
def count_integer(lst):
    return sum(isinstance(i, int) for i in lst)

# Test cases to verify the correctness of the function
assert count_integer([1,2,'abc',1.2]) == 2
assert count_integer(['hello', 3.14, True, 5]) == 2
assert count_integer([100, -200, 'Python', 300]) == 3
assert count_integer([]) == 0
assert count_integer([None, False, True, 0]) == 1