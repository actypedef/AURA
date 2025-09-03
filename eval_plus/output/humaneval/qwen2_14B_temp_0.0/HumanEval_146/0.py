
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
import re

def specialFilter(nums):
    def is_odd_digit(digit):
        return digit in '13579'

    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))  # Convert to string and handle negative numbers
            if is_odd_digit(num_str[0]) and is_odd_digit(num_str[-1]):
                count += 1
    return count

# Test cases