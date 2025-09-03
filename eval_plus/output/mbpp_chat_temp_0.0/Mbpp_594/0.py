"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
def diff_even_odd(nums):
    # Find the index of the first even number using list comprehension
    first_even = next((i for i, x in enumerate(nums) if x % 2 == 0), -1)
    
    # Find the index of the first odd number using list comprehension
    first_odd = next((i for i, x in enumerate(nums) if x % 2 != 0), -1)
    
    # Calculate the absolute difference between the indices of the first even and odd numbers
    return abs(first_even - first_odd)

# Test the function with the provided test case
assert diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 3