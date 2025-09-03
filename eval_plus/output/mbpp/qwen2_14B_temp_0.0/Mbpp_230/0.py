"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
def replace_blank(s, ch):
    # Replace spaces in the string with the given character
    s = s.replace(' ', ch)
    return s

# Test the function with the provided test case
assert replace_blank("hello people", '@') == "hello@people"
