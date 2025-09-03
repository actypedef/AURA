"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""
def remove_nested(test_tup):
    # Using list comprehension to filter out nested tuples
    res = tuple(ele for ele in test_tup if not isinstance(ele, tuple))
    return res

# Test the function with the provided test case
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
