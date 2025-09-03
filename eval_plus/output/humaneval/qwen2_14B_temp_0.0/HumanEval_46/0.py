

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
from typing import *
from collections import *

def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    """
    if n < 4:
        return [0, 0, 2, 0][n]
    
    # Initialize the first four elements of the sequence
    fib4_values = [0, 0, 2, 0]
    
    # Compute the sequence iteratively up to the n-th element
    for i in range(4, n + 1):
        next_value = sum(fib4_values)
        fib4_values.pop(0)  # Remove the oldest value
        fib4_values.append(next_value)  # Add the newest value
    
    return fib4_values[-1]

# Test cases