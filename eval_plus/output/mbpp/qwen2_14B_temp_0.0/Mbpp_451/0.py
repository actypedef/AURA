"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""
def remove_whitespaces(str1):
    # Use the replace method to remove all whitespaces
    str1 = str1.replace(" ", "")
    return str1

# Test the function with the provided test case
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
