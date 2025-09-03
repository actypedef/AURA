"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""
def median_numbers(x, y, z):
    # Create a list containing the three numbers
    numbers = [x, y, z]
    
    # Sort the list to arrange the numbers in ascending order
    numbers.sort()
    
    # Return the middle number as the median
    return numbers[1]

# Test the function with the provided test case
assert median_numbers(25, 55, 65) == 55.0
