
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
import re

def get_closest_vowel(word):
    # Define vowels
    vowels = "aeiouAEIOU"
    
    # Find all vowels that are surrounded by consonants
    matches = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU](?=[^aeiouAEIOU])', word)
    
    # Return the last match found, or an empty string if no match
    return matches[-1] if matches else ""

# Test cases