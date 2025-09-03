
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
    # Initialize variables to keep track of the word with maximum unique characters
    max_unique_count = 0
    result_word = ""
    
    for word in words:
        # Calculate the number of unique characters in the current word
        unique_chars = set(word)
        unique_count = len(unique_chars)
        
        # Check if this word has more unique characters than the current maximum
        if unique_count > max_unique_count or (unique_count == max_unique_count and word < result_word):
            max_unique_count = unique_count
            result_word = word
    
    return result_word

# Test cases