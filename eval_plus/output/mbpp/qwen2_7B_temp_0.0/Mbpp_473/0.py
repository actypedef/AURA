"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""
def tuple_intersection(test_list1, test_list2):
    # Convert each tuple in both lists to sorted tuples to ensure order doesn't matter
    res = set(map(tuple, map(sorted, test_list1))) & set(map(tuple, map(sorted, test_list2)))
    return res

# Test the function with the provided test case
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}