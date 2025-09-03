"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""
def first_odd(nums):
    # Use a generator expression to iterate through the list
    return next((num for num in nums if num % 2 != 0), None)

# Test the function with the provided test case
assert first_odd([1, 3, 5]) == 1
