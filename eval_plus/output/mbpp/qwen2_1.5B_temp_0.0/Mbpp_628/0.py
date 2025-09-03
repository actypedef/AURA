"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""
def replace_spaces(s):
    # Replace spaces with '%20' using the built-in str.replace() method
    return s.replace(' ', '%20')

# Test cases to verify the correctness of the solution
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
assert replace_spaces("Hello World!") == 'Hello%20World!'
assert replace_spaces("") == ''
assert replace_spaces("NoSpacesHere") == 'NoSpacesHere'