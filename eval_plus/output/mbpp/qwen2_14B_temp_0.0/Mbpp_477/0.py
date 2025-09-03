"""
Write a python function to convert the given string to lower case.
assert is_lower("InValid") == "invalid"
"""
def is_lower(s):
    # Convert the string to lower case
    s = s.lower()
    return s

# Test the function with the provided test case
assert is_lower("InValid") == "invalid"
