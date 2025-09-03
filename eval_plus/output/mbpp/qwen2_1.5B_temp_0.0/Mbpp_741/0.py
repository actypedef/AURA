"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
def all_characters_same(s):
    return len(set(s)) == 1

# Test cases
assert all_characters_same("python") == False
assert all_characters_same("aaaaa") == True
assert all_characters_same("abba") == True
assert all_characters_same("") == True
assert all_characters_same("12345") == False