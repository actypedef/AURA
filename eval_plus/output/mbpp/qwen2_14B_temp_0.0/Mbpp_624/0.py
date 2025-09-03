"""
Write a python function to convert a given string to uppercase.
assert is_upper("person") =="PERSON"
"""
def is_upper(str):
    # Convert the string to uppercase and return it
    str = str.upper()
    return (str)

# Test the function with the provided test case
assert is_upper("person") == "PERSON"
