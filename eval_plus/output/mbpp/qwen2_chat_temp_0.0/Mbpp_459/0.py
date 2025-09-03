"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""
def remove_uppercase(s):
    # Initialize an empty list to store characters
    result = []
    
    # Iterate through each character in the input string
    for char in s:
        # Check if the character is not uppercase
        if not char.isupper():
            # If it's not uppercase, append it to the result list
            result.append(char)
    
    # Join the list of characters into a single string and return it
    return ''.join(result)

# Test the function with the provided test case
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'