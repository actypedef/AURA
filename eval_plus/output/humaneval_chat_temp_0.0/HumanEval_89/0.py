
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
def encrypt(s):
    # Define the alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Initialize the encrypted string
    encrypted_string = ""
    
    # Iterate through each character in the input string
    for char in s:
        if char in alphabet:
            # Find the index of the character in the alphabet
            index = alphabet.index(char)
            # Calculate the new index after rotation
            new_index = (index + 2 * 2) % 26
            # Append the encrypted character to the result string
            encrypted_string += alphabet[new_index]
        else:
            # If the character is not in the alphabet, append it unchanged
            encrypted_string += char
    
    return encrypted_string

# Test cases