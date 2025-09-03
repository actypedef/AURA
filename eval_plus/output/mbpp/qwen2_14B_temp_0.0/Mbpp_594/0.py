"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
def diff_even_odd(nums):
    # Find the first even number in the list
    first_even = next((num for num in nums if num % 2 == 0), -1)
    # Find the first odd number in the list
    first_odd = next((num for num in nums if num % 2 != 0), -1)
    
    # Calculate and return the difference between the first even and first odd number
    return first_even - first_odd

# Test the function with the provided test case
assert diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 3
