"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(numbers):
    # Initialize variables to store the first even and odd numbers
    first_even = None
    first_odd = None
    
    # Iterate through each number in the list
    for num in numbers:
        if first_even is None and num % 2 == 0:
            first_even = num  # Assign the first even number found
        elif first_odd is None and num % 2 != 0:
            first_odd = num   # Assign the first odd number found
        
        # If both even and odd numbers are found, break out of the loop
        if first_even is not None and first_odd is not None:
            break
    
    # Return the product of the first even and odd numbers
    return first_even * first_odd

# Test the function with the provided test case
assert mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 4