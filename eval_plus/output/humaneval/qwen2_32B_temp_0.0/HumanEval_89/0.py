
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
    encrypted = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + 4) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + 4) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted

# Test cases
assert encrypt('hi') == 'lm'
assert encrypt('asdfghjkl') == 'ewhjklnop'
assert encrypt('gf') == 'kj'
assert encrypt('et') == 'ix'