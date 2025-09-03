

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
# Define the function to calculate the nth Fibonacci number
def fib(n: int):
    # Base cases for the first two numbers in the sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Calculate the nth Fibonacci number iteratively
    for _ in range(2, n + 1):
        # Update the values of a and b
        a, b = b, a + b
    
    # Return the nth Fibonacci number
    return b

# Test the function with provided data points
assert fib(10) == 55, "Test case 1 failed"
assert fib(1) == 1, "Test case 2 failed"
assert fib(8) == 21, "Test case 3 failed"
