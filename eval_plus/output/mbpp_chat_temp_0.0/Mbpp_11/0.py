"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
def remove_Occ(s, ch):
    # Find the index of the first occurrence of the character
    first_occurrence = s.find(ch)
    
    # If the character is not found, return the original string
    if first_occurrence == -1:
        return s
    
    # Remove the first occurrence
    s = s[:first_occurrence] + s[first_occurrence+1:]
    
    # Find the index of the last occurrence of the character
    last_occurrence = s.rfind(ch)
    
    # If the character is not found (which should not happen), return the modified string
    if last_occurrence == -1:
        return s
    
    # Remove the last occurrence
    s = s[:last_occurrence] + s[last_occurrence+1:]
    
    return s

# Test the function with the provided test case
assert remove_Occ("hello", "l") == "heo"