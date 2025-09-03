"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""
def get_Char(s):
    # Initialize sum to store the sum of ASCII values of characters
    sum = 0
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Add ASCII value of current character to sum
        sum += ord(s[i])
    
    # Calculate the result using modulo operation
    res = (sum % 26) + 97
    
    # Convert ASCII value back to character and return
    return chr(res)

# Test the function with the provided test case
assert get_Char("abc") == "f"
