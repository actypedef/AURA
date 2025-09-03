
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
import re

def words_string(s):
    # Use regular expression to split the string by either comma or space
    words = re.split(r'[ ,]', s)
    # Filter out any empty strings that may result from consecutive delimiters
    words = [word for word in words if word]
    return words

# Test cases