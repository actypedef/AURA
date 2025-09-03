"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""
def sum_negativenum(nums):
    return sum(num for num in nums if num < 0)

# Test cases
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
assert sum_negativenum([-1, -2, -3, -4, -5]) == -15
assert sum_negativenum([1, 2, 3, 4, 5]) == 0
assert sum_negativenum([]) == 0