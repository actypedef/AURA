
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
def is_equal_to_sum_even(n):
    # Check if n is even and greater than or equal to 8
    return n % 2 == 0 and n >= 8

# Test cases