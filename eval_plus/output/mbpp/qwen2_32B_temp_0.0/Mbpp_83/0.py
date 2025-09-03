"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""
def get_Char(s):
    total = sum(ord(c) for c in s)
    return chr((total % 26) + ord('a'))

assert get_Char("abc") == "f"
assert get_Char("hello") == "r"
assert get_Char("world") == "j"
assert get_Char("python") == "u"
assert get_Char("programming") == "i"
assert get_Char("is") == "i"
assert get_Char("fun") == "u"
assert get_Char("to") == "t"
assert get_Char("learn") == "l"
assert get_Char("python") == "u"