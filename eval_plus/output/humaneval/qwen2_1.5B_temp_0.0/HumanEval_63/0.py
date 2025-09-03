

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
def fibfib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        # Initialize the base cases
        fibfib_0 = 0
        fibfib_1 = 0
        fibfib_2 = 1
        
        # Compute the nth Fibonacci number using dynamic programming
        for i in range(3, n+1):
            fibfib_i = fibfib_0 + fibfib_1 + fibfib_2
            fibfib_0, fibfib_1, fibfib_2 = fibfib_1, fibfib_2, fibfib_i
        
        return fibfib_i

# Test cases