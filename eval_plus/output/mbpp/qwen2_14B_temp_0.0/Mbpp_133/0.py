"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""
def sum_negativenum(numbers):
    # Use a generator expression to filter negative numbers and sum them
    return sum(num for num in numbers if num < 0)

# Test the function with the provided test case
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
