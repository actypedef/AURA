"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""
def list_tuple(list1):
    # Convert the list to a tuple
    tuple1 = tuple(list1)
    return tuple1

# Test the function with the provided test case
assert list_tuple([5, 10, 7, 4, 15, 3]) == (5, 10, 7, 4, 15, 3)
