"""
Write a python function to convert the given string to lower case.
assert is_lower("InValid") == "invalid"
"""
def is_lower(string):
    # Convert the input string to lowercase using the str.lower() method
    return string.lower()

# Test the function with the provided test case
assert is_lower("InValid") == "invalid"
