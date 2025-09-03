"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""
def tuple_to_int(test_tup):
    # Convert each element of the tuple to a string and join them together
    res = int(''.join(map(str, test_tup)))
    return res

# Test the function with the provided test case
assert tuple_to_int((1, 2, 3)) == 123
