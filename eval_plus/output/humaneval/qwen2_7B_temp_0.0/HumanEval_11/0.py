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
    # Convert strings to lists of integers for easier manipulation
    list_a = [int(char) for char in a]
    list_b = [int(char) for char in b]

    # Ensure both lists have the same length by padding the shorter one with zeros
    max_length = max(len(list_a), len(list_b))
    list_a.extend([0] * (max_length - len(list_a)))
    list_b.extend([0] * (max_length - len(list_b)))

    # Perform XOR operation
    xor_result = [str(int(x) ^ int(y)) for x, y in zip(list_a, list_b)]

    # Join the list back into a string and return it
    return ''.join(xor_result)

# Test the function