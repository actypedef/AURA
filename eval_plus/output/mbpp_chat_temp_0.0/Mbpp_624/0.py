"""
Write a python function to convert a given string to uppercase.
assert is_upper("person") =="PERSON"
"""
def is_upper(string):
    # Convert the entire string to uppercase using the upper() method
    return string.upper()

# Test the function with the provided test case
assert is_upper("person") == "PERSON"
