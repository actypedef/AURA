"""
Write a python function to convert the given string to lower case.
assert is_lower("InValid") == "invalid"
"""
def is_lower(string):
    # Check if all characters in the string are lowercase
    return string.islower()

# Test the function with the provided test case
assert is_lower("InValid") == "invalid"
