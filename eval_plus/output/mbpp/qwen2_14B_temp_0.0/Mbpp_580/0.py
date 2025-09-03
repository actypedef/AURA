"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""
def extract_even(test_tup):
    # Filter out odd numbers at the top level of the tuple
    res = tuple(ele for ele in test_tup if isinstance(ele, int) and ele % 2 == 0 or not isinstance(ele, int))
    
    # Process nested tuples recursively
    res = tuple(extract_even(ele) if isinstance(ele, tuple) else ele for ele in res)
    
    return res

# Test the function with the provided test case
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
