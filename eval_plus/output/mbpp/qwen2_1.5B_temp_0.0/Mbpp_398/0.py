"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""
def sum_of_digits(numbers):
    """
    Compute the sum of digits of each number in a given list.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The sum of all digits in the list.
    """
    total_sum = 0
    for num in numbers:
        while num > 0:
            digit = num % 10
            total_sum += digit
            num //= 10
    return total_sum

# Test cases
assert sum_of_digits([10,2,56]) == 14
assert sum_of_digits([1,23,456789]) == 45
assert sum_of_digits([-10,20,-30]) == 6
assert sum_of_digits([0,0,0]) == 0
assert sum_of_digits([]) == 0