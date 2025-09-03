"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""
import re

def find_adverb_position(text):
    # Use regular expression to find all occurrences of words ending in 'ly'
    for match in re.finditer(r"\w+ly", text):
        # Return the start and end positions along with the matched adverb
        return (match.start(), match.end(), match.group(0))

# Test the function with the provided test case
assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
