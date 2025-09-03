"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(s):
    # Initialize an empty list to store even-indexed characters
    result = []
    
    # Iterate over the string using enumerate to get both index and character
    for i, char in enumerate(s):
        # Check if the index is even (i.e., character position is even)
        if i % 2 == 0:
            # Append the character at the even index to the result list
            result.append(char)
    
    # Join the list of characters into a single string and return it
    return ''.join(result)

# Test the function with the provided test case
assert remove_odd("python") == "yhn"
