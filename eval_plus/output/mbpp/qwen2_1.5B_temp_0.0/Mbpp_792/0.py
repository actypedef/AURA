"""
Write a python function to count the number of lists in a given number of lists.
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""
def count_list(lists):
    return len(lists)

# Test cases
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4