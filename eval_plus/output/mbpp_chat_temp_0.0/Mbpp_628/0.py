"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""
def replace_spaces(input_string):
    # Replace each space character in the input string with '%20'
    return input_string.replace(' ', '%20')

# Test the function with the provided test case
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
