"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""
import re

def max_run_uppercase(s):
    # Find all sequences of uppercase letters in the string
    upper_runs = re.findall('[A-Z]+', s)
    
    # Find the length of the longest sequence
    max_upper_run = max(len(run) for run in upper_runs)
    
    return max_upper_run

# Test the function with the provided test case
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
