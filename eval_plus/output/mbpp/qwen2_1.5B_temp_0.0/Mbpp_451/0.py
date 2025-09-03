"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""
def remove_whitespaces(input_string):
    # Use the replace method to remove all whitespace characters
    return input_string.replace(" ", "")

# Test cases to verify the correctness of the solution
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
assert remove_whitespaces('  Hello   World!  ') == 'HelloWorld!'
assert remove_whitespaces('Python 3.8') == 'Python3.8'
assert remove_whitespaces('') == ''