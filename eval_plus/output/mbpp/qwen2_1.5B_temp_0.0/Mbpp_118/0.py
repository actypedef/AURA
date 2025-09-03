"""
Write a function to convert a string to a list of strings split on the space character.
assert string_to_list("python programming")==['python','programming']
"""
def string_to_list(s):
    return s.split()

# Test cases
assert string_to_list("python programming") == ['python', 'programming']
assert string_to_list("hello world") == ['hello', 'world']
assert string_to_list("") == []
assert string_to_list("singleword") == ['singleword']