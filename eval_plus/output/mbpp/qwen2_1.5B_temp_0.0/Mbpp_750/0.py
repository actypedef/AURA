"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""
def add_tuple(lst, tup):
    # Append the tuple to the list
    lst.append(tup)
    return lst

# Test cases to verify the correctness of the function
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
assert add_tuple([], (1, 2)) == [1, 2]
assert add_tuple(['a', 'b'], ('c', 'd')) == ['a', 'b', 'c', 'd']