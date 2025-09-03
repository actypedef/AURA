

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
def add(x: int, y: int) -> int:
    """Add two numbers x and y

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.

    Examples:
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

# Test cases to verify the correctness of the function
assert add(2, 3) == 5, "Test case 1 failed"
assert add(5, 7) == 12, "Test case 2 failed"
