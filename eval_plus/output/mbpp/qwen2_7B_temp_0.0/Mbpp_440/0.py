"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""
import re

def find_adverb_position(sentence):
    # Use regular expression to find all occurrences of words ending with 'ly'
    adverbs = re.findall(r"\w+ly", sentence)
    
    if len(adverbs) > 0:
        # Return the position of the first adverb found
        return (sentence.index(adverbs[0]), 
                sentence.index(adverbs[0]) + len(adverbs[0]), 
                adverbs[0])
    else:
        # If no adverbs are found, return None for each position
        return (None, None, None)

# Test the function with the provided test case
assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
