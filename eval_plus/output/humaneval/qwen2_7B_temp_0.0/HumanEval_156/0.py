
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
# Importing necessary library
from typing import List

def int_to_mini_roman(number: int) -> str:
    """
    Convert an integer to its Roman numeral representation in lowercase.
    
    Args:
    number (int): The integer to convert, must be between 1 and 1000 inclusive.

    Returns:
    str: The Roman numeral representation of the integer in lowercase.
    """
    # Define Roman numeral mappings
    val_map = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    
    # Build the Roman numeral string
    roman_numeral = ''
    for value in sorted(val_map.keys(), reverse=True):
        while number >= value:
            number -= value
            roman_numeral += val_map[value]
    
    return roman_numeral

# Check function to verify the correctness of the solution
def check():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    print("All tests passed!")

# Run the check function
check()