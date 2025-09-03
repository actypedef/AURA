"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(nums):
    # Initialize variables to store the first even and odd numbers found
    first_even = None
    first_odd = None
    
    # Iterate through each number in the list
    for num in nums:
        if first_even is None and num % 2 == 0:  # Check if it's the first even number
            first_even = num
        elif first_odd is None and num % 2 != 0:  # Check if it's the first odd number
            first_odd = num
    
    # Calculate the product of the first even and odd numbers
    return first_even * first_odd

# Test the function with the provided test case
assert mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 4
