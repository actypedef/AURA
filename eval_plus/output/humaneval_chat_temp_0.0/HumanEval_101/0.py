
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
    """
    Splits a string of words separated by commas or spaces into an array of words.

    Args:
    s (str): A string containing words separated by commas or spaces.

    Returns:
    list: An array of words extracted from the input string.

    Examples:
    >>> words_string("Hi, my name is John")
    ['Hi', 'my', 'name', 'is', 'John']
    >>> words_string("One, two, three, four, five, six")
    ['One', 'two', 'three', 'four', 'five', 'six']
    """
    # Use regular expression to split the string by either comma or space
    return re.split(r'[,\s]+', s)

# Check function to verify the correctness of the solution
def check():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    print("All tests passed!")

check()