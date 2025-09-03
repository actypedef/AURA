"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""
def remove_odd(nums):
    # Use list comprehension to filter out odd numbers
    return [num for num in nums if num % 2 == 0]

# Test the function with the provided test case
assert remove_odd([1, 2, 3]) == [2]
