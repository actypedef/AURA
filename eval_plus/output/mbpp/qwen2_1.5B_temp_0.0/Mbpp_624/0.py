"""
Write a python function to convert a given string to uppercase.
assert is_upper("person") =="PERSON"
"""
def is_upper(s):
    return s.upper() == s

# Test cases
assert is_upper("person") == "PERSON"
assert is_upper("Hello World!") == "HELLO WORLD!"
assert is_upper("12345") == "12345"
assert is_upper("") == ""
assert is_upper("Python 3.8") == "PYTHON 3.8"