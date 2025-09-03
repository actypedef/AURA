"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""
def sum_of_digits(nums):
    # Calculate the sum of digits for each number in the list
    return sum(int(digit) for num in nums for digit in str(num))

# Test the function with the provided test case
assert sum_of_digits([10, 2, 56]) == 14
