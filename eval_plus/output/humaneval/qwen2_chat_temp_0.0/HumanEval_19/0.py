from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
from typing import *
from collections import *

def sort_numbers(numbers: str) -> str:
    # Mapping of words to their numeric values
    word_to_num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    # Splitting the input string into a list of words
    words = numbers.split()
    
    # Sorting the list based on the numeric value of each word
    sorted_words = sorted(words, key=lambda word: word_to_num[word])
    
    # Joining the sorted words back into a single string
    return ' '.join(sorted_words)

# Test cases