"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""
def remove_whitespaces(str1):
    # Use the replace method to substitute all whitespace characters with an empty string
    return str1.replace(" ", "")

# Test the function with the provided test case
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
