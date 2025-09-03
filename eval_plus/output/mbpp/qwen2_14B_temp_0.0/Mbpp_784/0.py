"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(nums):
    # Initialize variables to store the first even and odd numbers
    first_even = -1
    first_odd = -1
    
    # Iterate through the list to find the first even and odd numbers
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            first_even = nums[i]
            break
    
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            first_odd = nums[i]
            break
    
    # Return the product of the first even and odd numbers
    return first_even * first_odd

# Test the function with the provided test case
assert mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 4
