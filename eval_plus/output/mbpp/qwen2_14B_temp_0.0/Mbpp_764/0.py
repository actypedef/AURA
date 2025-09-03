"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""
import re

def number_ctr(str):
    # Use regex to find all digits in the string and return their count
    return len(re.findall(r'\d', str))

# Test the function with the provided test case
assert number_ctr('program2bedone') == 1
