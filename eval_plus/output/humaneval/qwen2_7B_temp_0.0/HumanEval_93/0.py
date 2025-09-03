
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
    # Define the mapping for vowels to their corresponding encoded characters
    vowel_mapping = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    
    # Initialize an empty string to store the encoded message
    encoded_message = ''
    
    # Iterate over each character in the input message
    for char in message:
        # Swap the case of the character
        if char.islower():
            swapped_char = char.upper()
        else:
            swapped_char = char.lower()
        
        # Check if the swapped character is a vowel
        if swapped_char in vowel_mapping:
            # Replace the vowel with its corresponding encoded character
            encoded_message += vowel_mapping[swapped_char]
        else:
            # If it's not a vowel, just add the swapped character as is
            encoded_message += swapped_char
    
    return encoded_message

# Test cases