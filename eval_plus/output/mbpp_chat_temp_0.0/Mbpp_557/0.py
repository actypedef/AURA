"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(s):
    # Initialize an empty list to store the modified characters
    result = []
    
    # Iterate through each character in the input string
    for char in s:
        # Check if the character is lowercase
        if char.islower():
            # Convert to uppercase and add to the result list
            result.append(char.upper())
        else:
            # Convert to lowercase and add to the result list
            result.append(char.lower())
    
    # Join the list into a string and return it
    return ''.join(result)

# Test the function with the provided test case
assert toggle_string("Python") == "pYTHON"
