
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
    # Define vowels and their next two vowels
    vowels = "aeiouAEIOU"
    next_vowels = [vowel + "2" for vowel in vowels]
    
    # Swap case and replace vowels
    encoded_message = ''.join([char.swapcase() if char in vowels else next_vowels[vowels.index(char)] if char in next_vowels else char for char in message])
    
    return encoded_message

# Test cases