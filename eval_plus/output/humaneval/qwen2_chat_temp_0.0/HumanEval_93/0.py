
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
def encode(message):
    """
    Encode a given message by swapping the case of all letters and replacing each vowel with the letter two places ahead in the English alphabet.
    
    Args:
    message (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    # Define the mapping for vowel replacement
    vowel_map = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    result = []

    # Iterate through each character in the message
    for char in message:
        if char.isalpha():
            # Swap the case of the character
            swapped_char = char.swapcase()
            # Replace the vowel using the map if it's a vowel
            if swapped_char.lower() in vowel_map:
                result.append(vowel_map[swapped_char.lower()].swapcase())
            else:
                result.append(swapped_char)
        else:
            result.append(char)

    return ''.join(result)

# Test cases