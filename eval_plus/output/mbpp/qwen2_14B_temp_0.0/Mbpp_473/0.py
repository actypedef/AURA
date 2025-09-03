"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""
def tuple_intersection(test_list1, test_list2):
    # Convert each tuple in both lists to a sorted tuple to ensure order doesn't matter
    # Then convert the lists of sorted tuples to sets and find the intersection
    res = set(tuple(sorted(sub)) for sub in test_list1) & set(tuple(sorted(sub)) for sub in test_list2)
    return res

# Test the function with the provided test case
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
