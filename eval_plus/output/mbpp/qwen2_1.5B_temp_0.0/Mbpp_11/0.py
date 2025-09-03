"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
def remove_Occ(text, char):
    # Remove first occurrence
    text = text.replace(char, '', 1)
    # Remove last occurrence
    text = text.replace(char, '', -1)
    return text

# Test cases
assert remove_Occ("hello", "l") == "heo"
assert remove_Occ("world", "o") == "world"
assert remove_Occ("python", "p") == "ython"
assert remove_Occ("java", "a") == "jav"
assert remove_Occ("programming", "g") == "programmin"