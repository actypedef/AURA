"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""
def new_tuple(string_list, element):
    # Create a new tuple using the provided string list and the additional element
    result = tuple(string_list) + (element,)
    return result

# Test cases to verify the correctness of the solution
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
assert new_tuple([], "test") == ('test',)
assert new_tuple(["apple", "banana"], "cherry") == ('apple', 'banana', 'cherry')