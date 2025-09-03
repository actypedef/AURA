"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""
import re

def match_a_followed_by_anything_ending_in_b(text):
    """
    Matches a string that starts with 'a', followed by any characters (including none), and ends with 'b'.
    
    Args:
    text (str): The input string to be matched.
    
    Returns:
    bool: True if the string matches the pattern, False otherwise.
    """
    # Define the regex pattern
    pattern = r'^a.*b$'
    
    # Use re.match to check if the entire string matches the pattern
    return bool(re.match(pattern, text))

# Test cases to verify the correctness of the function
assert match_a_followed_by_anything_ending_in_b("aabbbb") == True
assert match_a_followed_by_anything_ending_in_b("ab") == True
assert match_a_followed_by_anything_ending_in_b("abc") == False
assert match_a_followed_by_anything_ending_in_b("a") == False
assert match_a_followed_by_anything_ending_in_b("") == False