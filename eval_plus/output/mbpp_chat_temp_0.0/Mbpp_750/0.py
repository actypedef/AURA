"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""
def add_tuple(test_list, test_tup):
    # Extend the list by appending each element of the tuple
    test_list.extend(test_tup)
    return test_list

# Test the function with the provided test case
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
