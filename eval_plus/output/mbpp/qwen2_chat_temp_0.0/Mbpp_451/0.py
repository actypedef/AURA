"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""
def remove_whitespaces(s):
    # Use the replace method to remove all whitespace characters from the string
    return s.replace(" ", "")

# Test the function with the provided test case
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
