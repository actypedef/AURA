"""
Write a function to filter odd numbers.
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
"""
def filter_oddnumbers(nums):
    # Use list comprehension to filter out even numbers and keep only odd numbers
    return [num for num in nums if num % 2 != 0]

# Test the function with the provided test case
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
