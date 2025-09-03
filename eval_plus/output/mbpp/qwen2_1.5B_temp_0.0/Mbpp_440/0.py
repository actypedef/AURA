"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""
import re

def find_adverb_position(sentence):
    # Regular expression pattern to match adverbs at the beginning of a word
    pattern = r'\b\w+ly\b'
    matches = re.finditer(pattern, sentence)
    
    # Initialize variables to store the position and the adverb
    position = None
    adverb = None
    
    # Iterate over all matches found
    for match in matches:
        # Update the position and adverb if this match is earlier than the current one
        if position is None or match.start() < position:
            position = match.start()
            adverb = match.group(0)
    
    return (position, position + len(adverb), adverb)

# Test the function with the provided test case
assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')