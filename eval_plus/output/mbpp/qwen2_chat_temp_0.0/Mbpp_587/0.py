"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""
def list_tuple(test_list):
    # Convert the list to a tuple using tuple() constructor
    res = tuple(test_list)
    return res

# Test the function with the provided test case
assert list_tuple([5, 10, 7, 4, 15, 3]) == (5, 10, 7, 4, 15, 3)
