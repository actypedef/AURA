

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
# Define the fib4 function without using recursion
def fib4(n: int):
    # Base cases for the first four elements of the sequence
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 0
    elif n == 3:
        return 2
    else:
        # Initialize the first four values of the sequence
        a, b, c = 0, 0, 2
        # Compute the next elements iteratively
        for _ in range(4, n+1):
            a, b, c = b, c, a + b + c
        return c

# Test the function with provided data points
assert fib4(5) == 4
assert fib4(6) == 8
assert fib4(7) == 14