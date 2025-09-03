"""
Write a python function to convert the given string to lower case.
assert is_lower("InValid") == "invalid"
"""
def is_lower(s):
    return s.lower()

# Test cases
assert is_lower("InValid") == "invalid"
assert is_lower("HelloWorld") == "helloworld"
assert is_lower("123abcABC") == "123abcabc"
assert is_lower("") == ""
assert is_lower("Python3.8") == "python3.8"
