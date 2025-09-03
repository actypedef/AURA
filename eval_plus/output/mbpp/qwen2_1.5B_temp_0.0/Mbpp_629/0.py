"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""
def Split(numbers):
    return [num for num in numbers if num % 2 == 0]

# Test cases
assert Split([1,2,3,4,5]) == [2,4]
assert Split([10,22,33,44,55]) == [10,22,44]
assert Split([-1,-2,-3,-4,-5]) == [-2,-4]
assert Split([]) == []