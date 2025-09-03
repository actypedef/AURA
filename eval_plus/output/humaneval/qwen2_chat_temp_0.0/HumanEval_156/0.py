
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
    number (int): A positive integer between 1 and 1000 inclusive.
    
    Returns:
    str: The Roman numeral representation of the number in lowercase.
    """
    # Define the mapping from integers to Roman numerals
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "m", "cm", "d", "cd",
        "c", "xc", "l", "xl",
        "x", "ix", "v", "iv",
        "i"
    ]
    
    roman_numeral = ''
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman_numeral += syms[i]
            number -= val[i]
        i += 1
    return roman_numeral

# Check function to verify the correctness of the solution
def check_solution():
    test_cases = {
        19: 'xix',
        152: 'clii',
        426: 'cdxxvi',
    }
    
    for number, expected in test_cases.items():
        result = int_to_mini_roman(number)
        assert result == expected, f"Failed for {number}: expected {expected}, got {result}"
    print("All test cases passed!")

# Run the check function to validate the solution
check_solution()