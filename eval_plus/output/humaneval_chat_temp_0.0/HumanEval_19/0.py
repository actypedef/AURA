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
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Mapping of number words to their numeric values
    num_map = {
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
    
    # Split the input string into a list of number words
    num_words = numbers.split()
    
    # Convert number words to their numeric values
    nums = [num_map[word] for word in num_words]
    
    # Sort the numeric values
    nums.sort()
    
    # Convert the sorted numeric values back to number words
    sorted_num_words = [list(num_map.keys())[list(num_map.values()).index(n)] for n in nums]
    
    # Join the sorted number words into a single string
    return ' '.join(sorted_num_words)

# Test the function