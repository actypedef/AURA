
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
# Import necessary libraries
import re

def words_string(s):
    """
    Split the input string into words using commas or spaces as delimiters.
    
    Args:
    s (str): A string containing words separated by commas or spaces.
    
    Returns:
    list: An array of words extracted from the input string.
    """
    # Use regular expression to split the string by either comma or space
    words = re.split(r'[ ,]+', s)
    return words

# Test cases to verify the correctness of the solution
assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
