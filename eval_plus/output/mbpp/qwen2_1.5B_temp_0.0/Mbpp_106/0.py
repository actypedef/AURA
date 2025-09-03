"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""
def add_lists(list_to_append, tuple_to_add):
    # Convert the tuple to a list to allow appending
    converted_tuple = list(tuple_to_add)
    # Append the list to the converted tuple
    converted_tuple.extend(list_to_append)
    # Return the modified tuple as a tuple again
    return tuple(converted_tuple)

# Test cases to verify the correctness of the solution
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
assert add_lists(['a', 'b'], ('c', 'd')) == ('c', 'd', 'a', 'b')
assert add_lists([], (1, 2, 3)) == (1, 2, 3)
assert add_lists([100], ()) == (100,)