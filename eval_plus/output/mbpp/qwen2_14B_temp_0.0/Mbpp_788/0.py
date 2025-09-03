"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""
def new_tuple(test_list, test_str):
    # Create a new tuple by combining the list and the string
    res = tuple(test_list + [test_str])
    return res

# Test the function with the provided test case
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
