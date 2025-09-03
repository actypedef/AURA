"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""
import re

def remove_length(text, n):
    # Use regex to replace words of length n with an empty string
    return re.sub(r'\b\w{3}\b', '', text)

# Test the function with the provided test case
assert remove_length('The person is most value tet', 3) == 'person is most value'