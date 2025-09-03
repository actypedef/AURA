"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(s):
    # Initialize an empty result string
    result = ""
    
    # Iterate through each character in the input string
    for i in range(len(s)):
        # Check if the character is lowercase
        if s[i].islower():
            # Convert to uppercase and append to result
            result += s[i].upper()
        else:
            # Convert to lowercase and append to result
            result += s[i].lower()
    
    return result

# Test the function with the provided test case
assert toggle_string("Python") == "pYTHON"
