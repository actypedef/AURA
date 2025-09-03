"""
Write a function to find cubes of individual elements in a list.
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""
def cube_nums(nums):
    # Apply the cube operation to each element in the list using list comprehension
    cube_nums = [num ** 3 for num in nums]
    return cube_nums

# Test the function with the provided test case
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
