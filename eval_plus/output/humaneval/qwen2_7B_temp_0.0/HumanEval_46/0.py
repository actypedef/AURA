

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
def fib4(n: int) -> int:
    """Efficiently computes the n-th element of the fib4 number sequence without using recursion."""
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize the first four values of the fib4 sequence
        fib_sequence = [0, 0, 2, 0]
        
        # Compute the fib4 sequence up to the n-th element
        for i in range(4, n + 1):
            next_value = sum(fib_sequence[-4:])  # Sum the last four elements to get the next value
            fib_sequence.append(next_value)
        
        return fib_sequence[n]

# Test cases
assert fib4(5) == 4
assert fib4(6) == 8
assert fib4(7) == 14
