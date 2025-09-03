"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""
def number_ctr(s):
    return len([char for char in s if char.isdigit()])