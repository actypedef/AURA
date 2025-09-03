"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""
def max_Product(arr):
    # Initialize two variables to store the maximum and second maximum elements
    x = y = float('-inf')
    
    # Iterate through each element in the array
    for i in arr:
        # Update the maximum and second maximum if the current element is greater
        if i > x:
            y = x  # Move the old maximum to the second maximum
            x = i  # Update the new maximum
        elif i > y:
            y = i  # Update the second maximum if the current element is between x and y
    
    # Return the pair of numbers with the highest product
    return (x, y)

# Test the function with the provided test case
assert max_Product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)