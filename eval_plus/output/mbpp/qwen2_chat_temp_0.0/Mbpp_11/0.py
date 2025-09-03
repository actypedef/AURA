"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
def remove_Occ(s, ch):
    # Find the index of the first occurrence of 'ch' in 's'
    first_occ = s.find(ch)
    
    # If 'ch' is not found, return the original string
    if first_occ == -1:
        return s
    
    # Remove the first occurrence of 'ch' by slicing the string
    s = s[:first_occ] + s[first_occ+1:]
    
    # Find the index of the last occurrence of 'ch' in the modified string
    last_occ = s.rfind(ch)
    
    # If 'ch' is not found (which should not happen), return the modified string
    if last_occ == -1:
        return s
    
    # Remove the last occurrence of 'ch' by slicing the string again
    s = s[:last_occ] + s[last_occ+1:]
    
    return s

# Test the function with the provided test case
assert remove_Occ("hello", "l") == "heo"
