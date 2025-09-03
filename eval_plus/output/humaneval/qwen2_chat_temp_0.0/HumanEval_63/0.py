

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
def fibfib(n: int) -> int:
    # Base cases for the sequence
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize the first three elements of the sequence
    a, b, c = 0, 0, 1
    
    # Compute the n-th element using iteration
    for _ in range(3, n + 1):
        next_value = a + b + c
        a, b, c = b, c, next_value
    
    return c

# Test cases to verify the correctness of the function
assert fibfib(1) == 0
assert fibfib(5) == 4
assert fibfib(8) == 24