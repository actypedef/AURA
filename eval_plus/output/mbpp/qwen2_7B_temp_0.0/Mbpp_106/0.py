"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""
def add_lists(lists, tup):
    # Convert the tuple to a list, concatenate it with the given list, and then convert it back to a tuple
    return tuple(list(tup) + lists)

# Test the function with the provided test case
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
