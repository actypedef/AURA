"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
import re

def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None

# Test cases
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
assert find_literals('Hello world!', 'world') == ('world', 7, 12)
assert find_literals('Python programming is fun.', 'fun') == ('fun', 30, 34)
assert find_literals('No match here.', 'not found') == None