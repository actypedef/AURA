"""
Write a function to convert a string to a list of strings split on the space character.
assert string_to_list("python programming")==['python','programming']
"""
def string_to_list(string):
    # Split the input string into a list using space as the delimiter
    return string.split(' ')

# Test the function with the provided test case
assert string_to_list("python programming") == ['python', 'programming']
