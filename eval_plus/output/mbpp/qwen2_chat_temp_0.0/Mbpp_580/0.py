"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""
def extract_even(test_tup):
    # Recursively filter out odd numbers from the nested tuple
    res = tuple(filter(lambda ele: ele % 2 == 0, test_tup))
    
    # Iterate through each element in the result tuple
    for ele in res:
        if isinstance(ele, tuple):
            # Recursively call the function if the element is a tuple
            res = tuple(map(extract_even, [ele]))
    
    return res

# Test the function with the provided test case
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)