"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
import re

def find_literals(text, pattern):
    # Use regular expression to find all occurrences of the pattern
    matches = re.findall(pattern, text)
    
    # If no match is found, return None
    if not matches:
        return None
    
    # Return the first match along with its start and end indices
    match = matches[0]
    start_index = text.index(match)
    end_index = start_index + len(match)
    
    return (match, start_index, end_index)

# Test the function with the provided test case
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
