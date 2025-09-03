"""
Write a function to convert a given string to a tuple of characters.
assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
"""
def string_to_tuple(str):
    # Convert the input string into a tuple of its characters
    return tuple(str)

# Test the function with the provided test case
assert string_to_tuple("python 3.0") == ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
