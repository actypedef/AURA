
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
def get_closest_vowel(word):
    # Define vowels
    vowels = 'aeiouAEIOU'
    # Iterate over the word from right to left
    for i in range(len(word) - 1, 0, -1):
        # Check if the current character is a vowel
        if word[i] in vowels:
            # If it's not the first or last character and it's a vowel
            if i > 0 and i < len(word) - 1:
                return word[i]
    # Return an empty string if no vowel is found
    return ''

# Test cases
assert get_closest_vowel("yogurt") == "u"
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("ab") == ""
