from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
from typing import *
from collections import *

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings are of equal length
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length")
    
    # Perform XOR operation character by character
    result = ''.join('1' if x != y else '0' for x, y in zip(a, b))
    
    return result

# Test cases to verify the correctness of the function
assert string_xor('010', '110') == '100'
assert string_xor('10101', '00111') == '10010'
assert string_xor('1111', '0000') == '1111'
assert string_xor('0000', '1111') == '1111'
assert string_xor('1111', '1111') == '0000'