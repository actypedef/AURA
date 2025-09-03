"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""
def first_odd(numbers):
    # Iterate through each number in the list
    for num in numbers:
        # Check if the number is odd
        if num % 2 != 0:
            return num

# Test the function with the provided test case
assert first_odd([1, 3, 5]) == 1
