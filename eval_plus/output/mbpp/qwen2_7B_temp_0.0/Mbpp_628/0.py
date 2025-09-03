"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""
def replace_spaces(string):
    # Replace each space character with '%20' using the str.replace() method
    return string.replace(' ', '%20')

# Test cases to verify the solution
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
