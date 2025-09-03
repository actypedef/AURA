"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""
def replace_char(string, old_char, new_char):
    # Replace all occurrences of old_char with new_char in the string
    string = string.replace(old_char, new_char)
    return string

# Test the function with the provided test case
assert replace_char("polygon", 'y', 'l') == "pollgon"
