"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""
def test_three_equal(x, y, z):
    # Initialize a counter for equal numbers
    count = 0
    
    # Check if x is equal to y and increment the counter
    if x == y:
        count += 1
    
    # Check if y is equal to z and increment the counter
    if y == z:
        count += 1
    
    # Check if x is equal to z and increment the counter
    if x == z:
        count += 1
    
    # Return the total count of equal numbers
    return count

# Test the function with the provided test case
assert test_three_equal(1, 1, 1) == 3
