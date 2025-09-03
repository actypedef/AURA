
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
    # Define the mapping for vowels to their corresponding characters two places ahead
    vowel_mapping = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    
    # Initialize an empty list to store encoded characters
    encoded_chars = []
    
    # Iterate over each character in the input message
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            # Swap the case of the character
            swapped_char = char.swapcase()
            
            # If the swapped character is a vowel, replace it using the mapping
            if swapped_char in vowel_mapping:
                encoded_chars.append(vowel_mapping[swapped_char])
            else:
                # Otherwise, keep the swapped character as is
                encoded_chars.append(swapped_char)
        else:
            # If the character is not a letter, raise an error (assuming only letters are provided)
            raise ValueError("Input contains non-letter characters")
    
    # Join the list of encoded characters into a single string and return it
    return ''.join(encoded_chars)

# Test cases