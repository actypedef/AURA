"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(lst):
    # Initialize variables to store the first even and odd numbers
    first_even = None
    first_odd = None
    
    # Iterate through the list to find the first even and odd numbers
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            if first_even is None:
                first_even = num
        else:  # Check if the number is odd
            if first_odd is None:
                first_odd = num
    
    # Calculate the product of the first even and odd numbers
    if first_even is not None and first_odd is not None:
        return first_even * first_odd
    else:
        return "No even or odd numbers found"

# Test cases to verify the correctness of the function
assert mul_even_odd([1,3,5,7,4,1,6,8]) == 4
assert mul_even_odd([2,4,6,8,10]) == 16
assert mul_even_odd([1,3,5,7]) == "No even or odd numbers found"
assert mul_even_odd([]) == "No even or odd numbers found"