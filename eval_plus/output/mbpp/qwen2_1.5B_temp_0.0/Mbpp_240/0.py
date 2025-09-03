"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""
def replace_list(list1, list2):
    # Replace the last element of list1 with the elements of list2
    list1[-1:] = list2
    return list1

# Test cases to verify the correctness of the solution
assert replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
assert replace_list([1, 2, 3, 4, 5], [6, 7, 8, 9]) == [1, 2, 3, 4, 6, 7, 8, 9]
assert replace_list(['a', 'b', 'c'], ['d', 'e']) == ['a', 'b', 'c', 'd', 'e']