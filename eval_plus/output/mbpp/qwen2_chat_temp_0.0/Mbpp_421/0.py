"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""
def concatenate_tuple(test_tup):
    # Convert all elements in the tuple to strings and join them using '-'
    res = '-'.join(str(ele) for ele in test_tup)
    return res

# Test the function with the provided test case
assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'