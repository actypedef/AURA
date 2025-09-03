"""
Write a python function which takes a list of integers and only returns the odd ones.
assert Split([1,2,3,4,5,6]) == [1,3,5]
"""
def Split(numbers):
    return [num for num in numbers if num % 2 != 0]

# Test cases to verify the correctness of the function
assert Split([1,2,3,4,5,6]) == [1,3,5]
assert Split([10,22,33,44,55,66]) == [33,55]
assert Split([-1,-2,-3,-4,-5,-6]) == [-1,-3,-5]
assert Split([]) == []
assert Split([7]) == [7]