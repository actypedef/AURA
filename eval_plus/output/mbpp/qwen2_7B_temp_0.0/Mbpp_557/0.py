"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(str):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through each character in the input string
    for char in str:
        # Check if the character is uppercase
        if char.isupper():
            # Convert to lowercase and append to result
            result += char.lower()
        else:
            # Convert to uppercase and append to result
            result += char.upper()
    
    return result

# Test the function with the provided test case
assert toggle_string("Python") == "pYTHON"
