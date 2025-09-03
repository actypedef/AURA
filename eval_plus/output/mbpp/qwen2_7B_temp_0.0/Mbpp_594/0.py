"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
def diff_even_odd(nums):
    # Initialize variables to store the first even and first odd numbers found
    first_even = None
    first_odd = None
    
    # Iterate through each number in the list
    for num in nums:
        if first_even is None and num % 2 == 0:  # Check if it's the first even number
            first_even = num
        elif first_odd is None and num % 2 != 0:  # Check if it's the first odd number
            first_odd = num
        
        # If both first_even and first_odd have been found, break out of the loop
        if first_even is not None and first_odd is not None:
            break
    
    # Calculate the difference between the first even and first odd numbers
    return first_even - first_odd

# Test the function with the provided test case
assert diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 3