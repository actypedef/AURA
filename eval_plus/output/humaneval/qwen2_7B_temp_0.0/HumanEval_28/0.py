from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
from typing import *
from collections import *

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Test cases to verify the correctness of the function
assert concatenate([]) == '', "Test with empty list failed"
assert concatenate(['a', 'b', 'c']) == 'abc', "Test with ['a', 'b', 'c'] failed"