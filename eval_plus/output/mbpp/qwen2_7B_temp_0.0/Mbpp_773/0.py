"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""
import re

def occurance_substring(string, substring):
    # Use regular expression to find all occurrences of the substring
    matches = re.finditer(substring, string)
    
    # Check if any matches were found
    if not matches:
        return None
    
    # Get the first match (since we're looking for the first occurrence)
    match = next(matches)
    
    # Extract the matched text, start position, and end position
    matched_text = match.group(0)
    start_position = match.start()
    end_position = match.end()
    
    # Return the results as a tuple
    return (matched_text, start_position, end_position)

# Test the function with the provided test case
assert occurance_substring('python programming, python language', 'python') == ('python', 0, 6)