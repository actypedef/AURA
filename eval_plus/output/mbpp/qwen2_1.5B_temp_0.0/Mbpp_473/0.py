"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""
def tuple_intersection(tup1, tup2):
    # Convert tuples to sets for efficient intersection operation
    set1 = set(tup1)
    set2 = set(tup2)
    
    # Find the intersection of the two sets
    result_set = set1.intersection(set2)
    
    # Convert the resulting set back to a tuple
    result_tuple = tuple(result_set)
    
    return result_tuple

# Test the function with provided data points
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}