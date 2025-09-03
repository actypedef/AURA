"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""
def upper_ctr(s):
    return sum(1 for char in s if char.isupper())

# Test cases
assert upper_ctr('PYthon') == 1
assert upper_ctr('Hello World!') == 2
assert upper_ctr('1234567890') == 0
assert upper_ctr('Python3.8') == 3
assert upper_ctr('UPPERlower') == 4