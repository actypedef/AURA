"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""
def Split(lst):
    # Use list comprehension to filter out even numbers
    return [i for i in lst if i % 2 == 0]

# Test the function with the provided test case
assert Split([1, 2, 3, 4, 5]) == [2, 4]
