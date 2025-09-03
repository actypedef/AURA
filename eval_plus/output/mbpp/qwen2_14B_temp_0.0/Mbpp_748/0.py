"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""
import re

def capital_words_spaces(str1):
    # Use regex to find words starting with a capital letter and add a space before them
    return (re.sub(r"(\w)([A-Z])", r"\1 \2", str1))

# Test the function with the provided test case
assert capital_words_spaces("Python") == 'Python'
