"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""
def extract_even(test_tup):
    # Define a recursive lambda function to filter even numbers
    res = lambda x: x if isinstance(x, int) and x % 2 == 0 else tuple(filter(extract_even, x))
    
    # Use the recursive lambda function to filter the input tuple
    result = res(test_tup)
    
    return result

# Test the function with the provided test case
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
