"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
import re

def find_literals(text, pattern):
    # Search for the pattern in the text using regular expressions
    match = re.search(pattern, text)
    
    if match:
        # If a match is found, return the matched substring and its start and end indices
        return (match.group(), match.start(), match.end())
    else:
        # If no match is found, return None for all values
        return (None, None, None)

# Test the function with the provided test case
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
