"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
import re

def find_literals(text, pattern):
    # Iterate over all matches of the pattern in the text
    for match in re.finditer(pattern, text):
        s = match.start()  # Get the start index of the match
        e = match.end()    # Get the end index of the match
        # Return the matched substring and its start and end indices
        return (text[s:e], s, e)

# Test the function with the provided test case
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
