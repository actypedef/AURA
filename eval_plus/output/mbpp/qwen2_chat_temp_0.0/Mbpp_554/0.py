"""
Write a python function which takes a list of integers and only returns the odd ones.
assert Split([1,2,3,4,5,6]) == [1,3,5]
"""
def Split(lst):
    # Use list comprehension to filter out even numbers and keep only odd numbers
    return [i for i in lst if i % 2 != 0]

# Test the function with the provided test case
assert Split([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
