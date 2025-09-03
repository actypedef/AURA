
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
# Import necessary packages at the beginning of your script
# In this case, no external packages are needed.

def int_to_mini_roman(number):
    """
    Convert an integer to its Roman numeral representation in lowercase.
    
    Args:
    number (int): A positive integer between 1 and 1000 inclusive.
    
    Returns:
    str: The Roman numeral representation of the given integer in lowercase.
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
    
    # Initialize the result string
    roman_numeral = ''
    
    # Loop through each value-symbol pair
    for i in range(len(val)):
        # While the current value can be subtracted from the number
        while number >= val[i]:
            # Append the corresponding symbol to the result
            roman_numeral += syms[i]
            # Subtract the value from the number
            number -= val[i]
    
    return roman_numeral

# Check function to verify the correctness of the generated function
def check():
    assert int_to_mini_roman(19) == 'xix', "Test case 1 failed"
    assert int_to_mini_roman(152) == 'clii', "Test case 2 failed"
    assert int_to_mini_roman(426) == 'cdxxvi', "Test case 3 failed"

# Call the check function to validate the solution
check()