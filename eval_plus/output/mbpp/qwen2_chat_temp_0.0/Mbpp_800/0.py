"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
# Define a function to remove all whitespaces from a given string
def remove_all_spaces(str1):
    # Use the replace method to substitute all spaces with an empty string
    return str1.replace(" ", "")

# Test cases to validate the function
assert remove_all_spaces('python  program') == 'pythonprogram'
