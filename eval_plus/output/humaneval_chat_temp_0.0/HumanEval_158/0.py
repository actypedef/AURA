
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
def find_max(words):
    # Initialize variables to keep track of the word with max unique chars and its count
    max_unique_word = ""
    max_unique_count = 0
    
    for word in words:
        # Use set to find unique characters in the current word
        unique_chars = set(word)
        unique_count = len(unique_chars)
        
        # Check if this word has more unique characters or is lexicographically smaller
        if unique_count > max_unique_count or (unique_count == max_unique_count and word < max_unique_word):
            max_unique_word = word
            max_unique_count = unique_count
            
    return max_unique_word

# Test cases