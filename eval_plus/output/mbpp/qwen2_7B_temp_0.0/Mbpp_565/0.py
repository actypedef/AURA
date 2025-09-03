"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""
def split(s):
    # Initialize an empty list to store the characters of the string
    result = []
    
    # Iterate over each character in the string using a for loop
    for char in s:
        # Append each character to the result list
        result.append(char)
    
    return result

# Test the function with the provided test case
assert split('python') == ['p', 'y', 't', 'h', 'o', 'n']
