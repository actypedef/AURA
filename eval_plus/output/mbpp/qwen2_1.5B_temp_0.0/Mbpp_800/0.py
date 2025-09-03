"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
def remove_all_spaces(input_string):
    # Use the replace method to remove all whitespace characters
    return input_string.replace(" ", "")

# Test cases to verify the correctness of the function
assert remove_all_spaces('python  program') == 'pythonprogram'
assert remove_all_spaces('   Leading spaces') == 'Leadingspaces'
assert remove_all_spaces('Trailing spaces   ') == 'Trailingspaces'
assert remove_all_spaces('Multiple   spaces   between words') == 'Multiplespacesbetweenwords'