
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
import re

def check_if_last_char_is_a_letter(txt):
    """
    Check if the last character of a given string is an alphabetical character
    and is not part of a word. A word is defined as a sequence of characters
    separated by spaces.

    Args:
    txt (str): The input string to check.

    Returns:
    bool: True if the last character is a letter and not part of a word, False otherwise.
    """
    # Regular expression to match a single letter at the end of a string
    # that is not preceded by another letter or digit.
    pattern = re.compile(r'\b[a-zA-Z]\b$')
    
    return bool(pattern.search(txt))

# Test cases to verify the correctness of the function
assert check_if_last_char_is_a_letter("apple pie") == False
assert check_if_last_char_is_a_letter("apple pi e") == True
assert check_if_last_char_is_a_letter("apple pi e ") == False
assert check_if_last_char_is_a_letter("") == False