"""
Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
assert swap_numbers(10,20)==(20,10)
"""
def swap_numbers(a, b):
    """
    Swap the values of two numbers and return them as a tuple.

    Args:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    tuple: A tuple containing the second number followed by the first number.
    """
    return (b, a)

# Test cases to verify the correctness of the solution
assert swap_numbers(10, 20) == (20, 10)
assert swap_numbers(-5, 3) == (3, -5)
assert swap_numbers(7.5, 4.2) == (4.2, 7.5)