"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
def replace_blank(str1, ch):
    # Replace all occurrences of ' ' (space) with the specified character 'ch'
    return str1.replace(' ', ch)

# Test the function with the provided test case
assert replace_blank("hello people", '@') == "hello@people"
