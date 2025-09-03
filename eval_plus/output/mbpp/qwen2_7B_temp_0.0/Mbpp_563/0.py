"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""
import re

def extract_values(text):
    # Use regular expression to find all substrings enclosed in double quotes
    return re.findall(r'"([^"]+)"', text)

# Test the function with the provided test case
assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
