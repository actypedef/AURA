"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""
def replace_char(str1, old_char, new_char):
    # Replace occurrences of old_char with new_char in str1
    return str1.replace(old_char, new_char)

# Test the function with the provided test case
assert replace_char("polygon", 'y', 'l') == "pollgon"
