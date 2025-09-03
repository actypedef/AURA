
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
from typing import *
from collections import *

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    # Sort the words lexicographically first to ensure that if there are multiple
    # words with the same number of unique characters, the one that comes first
    # in lexicographical order is returned.
    words.sort()
    
    # Initialize variables to keep track of the word with the maximum number of
    # unique characters and the count of unique characters.
    max_word = ""
    max_unique_chars = 0
    
    for word in words:
        # Use set to get the unique characters in the word.
        unique_chars_count = len(set(word))
        
        # Update the max_word if the current word has more unique characters,
        # or if it has the same number but comes first lexicographically.
        if unique_chars_count > max_unique_chars or (unique_chars_count == max_unique_chars and word < max_word):
            max_word = word
            max_unique_chars = unique_chars_count
    
    return max_word

# Test cases