

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
from typing import *
from collections import *

def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    balance = 0
    for bracket in brackets:
        if bracket == '<':
            balance += 1
        elif bracket == '>':
            balance -= 1
        # If balance goes negative, there are more closing brackets than opening ones
        if balance < 0:
            return False
    # If balance is zero, all opening brackets have matching closing brackets
    return balance == 0

# Test cases