from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
from typing import List

def sort_numbers(numbers: str) -> str:
    # Define the order of numbers
    number_order = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    # Split the input string into individual numbers
    numbers_list = numbers.split()
    
    # Sort the list of numbers based on their order defined above
    sorted_numbers = sorted(numbers_list, key=number_order.index)
    
    # Join the sorted numbers back into a single string
    return ''.join(sorted_numbers)

# Test cases
assert sort_numbers('three one five') == 'one three five'
assert sort_numbers('nine eight seven six') == 'six seven eight nine'
assert sort_numbers('zero four two') == 'zero two four'