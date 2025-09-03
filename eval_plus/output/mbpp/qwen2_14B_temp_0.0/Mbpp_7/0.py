"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
import re

def find_char_long(text):
    # Use regex to find all words with 4 or more characters
    return re.findall(r"\w{4,}", text)

# Test the function with the provided test case
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
