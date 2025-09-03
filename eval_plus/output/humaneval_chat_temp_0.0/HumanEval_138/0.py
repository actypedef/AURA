
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
def is_equal_to_sum_even(n):
    # Check if n is less than the smallest possible sum of 4 positive even numbers (which is 2+2+2+2=8)
    if n < 8:
        return False
    # Check if n is even, since the sum of even numbers is always even
    return n % 2 == 0

# Test cases to verify the correctness of the function
assert is_equal_to_sum_even(4) == False, "Test case 1 failed"
assert is_equal_to_sum_even(6) == False, "Test case 2 failed"
assert is_equal_to_sum_even(8) == True, "Test case 3 passed"
assert is_equal_to_sum_even(10) == True, "Test case 4 passed"
assert is_equal_to_sum_even(14) == True, "Test case 5 passed"
