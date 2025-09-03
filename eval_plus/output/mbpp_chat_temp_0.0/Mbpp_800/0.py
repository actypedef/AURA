"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
def remove_all_spaces(str1):
    # Use the replace method to substitute all spaces (' ') with an empty string ('')
    return str1.replace(" ", "")

# Test the function with the provided test case
assert remove_all_spaces('python  program') == 'pythonprogram'
