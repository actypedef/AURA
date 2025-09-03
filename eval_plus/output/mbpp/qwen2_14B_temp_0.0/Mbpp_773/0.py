"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""
import re

def occurance_substring(text, sample):
    # Iterate over all matches of the sample in the text
    for match in re.finditer(sample, text):
        # Extract the start and end positions of the match
        s = match.start()
        e = match.end()
        # Return the matched substring and its positions
        return (text[s:e], s, e)
    
    # Return None if no match is found
    return None

# Test the function with the provided test case
assert occurance_substring('python programming, python language', 'python') == ('python', 0, 6)
