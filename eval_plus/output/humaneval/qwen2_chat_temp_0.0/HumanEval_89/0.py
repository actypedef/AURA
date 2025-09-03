
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
    result = ""
    for char in s:
        if char.isalpha():
            # Calculate the new character's ASCII value after rotation
            ascii_offset = ord(char) + (2 * 2)
            # Handle wrap-around for lowercase and uppercase letters
            if char.islower():
                ascii_offset = ascii_offset % 128
                if ascii_offset < ord('a'):
                    ascii_offset += 97
            else:
                ascii_offset = ascii_offset % 128
                if ascii_offset < ord('A'):
                    ascii_offset += 65
            result += chr(ascii_offset)
        else:
            result += char
    return result

# Test cases to verify the correctness of the function
assert encrypt('hi') == 'lm', "Test case 1 failed"
assert encrypt('asdfghjkl') == 'ewhjklnop', "Test case 2 failed"
assert encrypt('gf') == 'kj', "Test case 3 failed"
assert encrypt('et') == 'ix', "Test case 4 failed"
