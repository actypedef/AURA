
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
from typing import List

def find_max(words: List[str]) -> str:
    # Initialize variables to keep track of the word with max unique chars
    max_unique_word = ""
    max_unique_count = 0
    
    for word in words:
        # Use set to count unique characters in the current word
        unique_chars = len(set(word))
        
        # Update max_unique_word if the current word has more unique characters,
        # or if it's equal but comes first lexicographically
        if unique_chars > max_unique_count or (unique_chars == max_unique_count and word < max_unique_word):
            max_unique_word = word
            max_unique_count = unique_chars
            
    return max_unique_word

# Test cases
assert find_max(["name", "of", "string"]) == "string"
assert find_max(["name", "enam", "game"]) == "enam"
assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
