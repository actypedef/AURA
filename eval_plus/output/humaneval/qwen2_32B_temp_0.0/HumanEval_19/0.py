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
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map number names to their corresponding values
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # Split the input string into a list of number names
    number_names = numbers.split()

    # Sort the list of number names based on their corresponding values
    sorted_number_names = sorted(number_names, key=lambda x: number_map[x])

    # Join the sorted list of number names back into a string
    sorted_numbers = ' '.join(sorted_number_names)

    return sorted_numbers

# Test cases
assert sort_numbers('three one five') == 'one three five'
assert sort_numbers('nine eight seven') == 'seven eight nine'
assert sort_numbers('zero four two') == 'zero two four'
assert sort_numbers('six three nine') == 'three six nine'
assert sort_numbers('five one zero') == 'zero one five'