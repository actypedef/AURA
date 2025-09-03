
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
    Check if the last non-space character of a string is an alphabetical letter
    and not part of a word.

    Args:
    txt (str): The input string to check.

    Returns:
    bool: True if the last non-space character is an alphabetical letter and not part of a word,
          False otherwise.
    """
    # Use regex to find all occurrences of words ending with a letter
    matches = re.findall(r'\b[a-zA-Z]\b', txt)
    # Return True if there's at least one match and it's the last character
    return bool(matches) and txt.strip().endswith(matches[-1])

# Test cases to verify the correctness of the function
assert check_if_last_char_is_a_letter("apple pie") == False
assert check_if_last_char_is_a_letter("apple pi e") == True
assert check_if_last_char_is_a_letter("apple pi e ") == False
assert check_if_last_char_is_a_letter("") == False