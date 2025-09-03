"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""
def get_Char(s):
    return chr((sum(ord(c) for c in s) % 26 + 97))

# Test cases
assert get_Char("abc") == "f"
assert get_Char("xyz") == "b"
assert get_Char("hello") == "k"
assert get_Char("world") == "t"
assert get_Char("python") == "z"