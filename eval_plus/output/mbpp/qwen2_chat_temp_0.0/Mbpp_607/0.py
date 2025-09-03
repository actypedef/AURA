"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
import re

def find_literals(text, pattern):
    # Search for the pattern in the text using regular expression
    match = re.search(pattern, text)
    
    # If no match is found, return None
    if not match:
        return None
    
    # Extract the matched substring, start index, and end index
    matched_substring = match.group(0)
    start_index = match.start()
    end_index = match.end()
    
    # Return the results as a tuple
    return (matched_substring, start_index, end_index)

# Test the function with the provided test case
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)