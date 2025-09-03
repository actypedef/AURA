"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(s):
    # Initialize an empty string to store even-indexed characters
    s1 = ""
    
    # Iterate over the string using enumerate to get both index and character
    for i, c in enumerate(s):
        # Check if the index is even (i.e., character position is even)
        if i % 2 == 0:
            # Append the character at even index to the new string
            s1 += c
    
    # Return the string containing only even-indexed characters
    return s1

# Test the function with the provided test case
assert remove_odd("python") == "yhn"
