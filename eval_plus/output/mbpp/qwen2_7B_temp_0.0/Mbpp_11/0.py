"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
def remove_Occ(s, ch):
    # Find the index of the first occurrence of the character
    first_occurrence = s.find(ch)
    
    if first_occurrence != -1:
        # Remove the first occurrence of the character
        s = s[:first_occurrence] + s[first_occurrence + 1:]
    
    # Find the index of the last occurrence of the character
    last_occurrence = s.rfind(ch)
    
    if last_occurrence != -1:
        # Remove the last occurrence of the character
        s = s[:last_occurrence] + s[last_occurrence + 1:]
    
    return s

# Test the function with the provided test case
assert remove_Occ("hello", "l") == "heo"
