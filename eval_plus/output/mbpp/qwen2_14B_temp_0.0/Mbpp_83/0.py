"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""
def get_Char(s):
    # Initialize sum to store the sum of ASCII values
    sum = 0
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # Add the ASCII value of the character to sum
        sum += (ord(s[i]) - ord('a'))
    
    # Find the new character by taking modulo 26 and adding it to 'a'
    return chr(sum % 26 + ord('a'))

# Test the function with the provided test case
assert get_Char("abc") == "f"
