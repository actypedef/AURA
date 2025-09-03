"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
def replace_blank(string, char):
    # Replace all occurrences of blank space with the specified character
    return string.replace(' ', char)

# Test the function with the provided test case
assert replace_blank("hello people", '@') == "hello@people"
