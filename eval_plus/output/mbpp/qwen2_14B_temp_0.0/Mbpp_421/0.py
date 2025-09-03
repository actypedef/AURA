"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""
def concatenate_tuple(test_tup):
    # Join all elements of the tuple into a string separated by the delimiter '-'
    res = '-'.join(map(str, test_tup))
    return res

# Test the function with the provided test case
assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'
