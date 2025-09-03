"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""
import re

def extract_values(s):
    # Use regular expression to find all text within double quotes
    return re.findall(r'"(.*?)"', s)

# Test the function with the provided test case
assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
