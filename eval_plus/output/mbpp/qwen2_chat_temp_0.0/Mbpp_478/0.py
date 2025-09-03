"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
def remove_lowercase(s):
    # Use list comprehension to filter out lowercase characters
    result = ''.join([i for i in s if i.isupper()])
    return result

# Test the function with the provided test case
assert remove_lowercase("PYTHon") == 'PYTH'
