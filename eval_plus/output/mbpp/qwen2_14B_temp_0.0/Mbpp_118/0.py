"""
Write a function to convert a string to a list of strings split on the space character.
assert string_to_list("python programming")==['python','programming']
"""
def string_to_list(text):
    # Split the text by spaces and return the resulting list
    return text.split(' ')

# Test the function with the provided test case
assert string_to_list("python programming") == ['python', 'programming']
