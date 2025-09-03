
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
    # Check if the string is empty or ends with a space
    if not txt or txt.endswith(' '):
        return False
    
    # Use regex to find all words and their positions
    words = re.findall(r'\b\w+\b', txt)
    last_word_end_pos = len(txt) - 1
    
    # Check if the last character is a letter and not part of a word
    if last_word_end_pos >= 0 and txt[last_word_end_pos].isalpha():
        for word_start, word_end in words:
            if word_start <= last_word_end_pos < word_end:
                return False
        return True
    else:
        return False

# Test cases