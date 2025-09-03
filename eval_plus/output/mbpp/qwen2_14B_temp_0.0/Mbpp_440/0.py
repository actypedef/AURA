"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""
import re

def find_adverb_position(text):
    # Regex pattern to find words ending with 'ly'
    for m in re.finditer(r"\w+ly", text):
        # Return the start and end positions, along with the matched adverb
        return (m.start(), m.end(), m.group(0))

# Test the function with the provided test case
assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
