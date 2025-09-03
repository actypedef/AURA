"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""
def tuple_str_int(test_str):
    # Convert the string representation of a tuple into an actual tuple of integers
    res = tuple(int(num) for num in test_str.strip('()').split(', '))
    return res

# Test the function with the provided test case
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
