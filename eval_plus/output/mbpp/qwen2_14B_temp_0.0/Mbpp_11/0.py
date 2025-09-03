"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
def remove_Occ(string, char):
    # Remove the first occurrence of the character
    for i in range(len(string)):
        if (string[i] == char):
            string = string[:i] + string[i+1:]
            break
    
    # Remove the last occurrence of the character
    for i in range(len(string) - 1, -1, -1):
        if (string[i] == char):
            string = string[:i] + string[i+1:]
            break
    
    return string

# Test the function with the provided test case
assert remove_Occ("hello", "l") == "heo"
