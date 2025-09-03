"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""
def get_Char(s):
    # Initialize result variable
    res = 0
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Add ASCII value of current character to result
        res += ord(s[i])
    
    # Take modulo 26 of the result
    res %= 26
    
    # Convert ASCII value back to character and return
    return chr(res + ord('a'))

# Test the function with the provided test case
assert get_Char("abc") == "f"
