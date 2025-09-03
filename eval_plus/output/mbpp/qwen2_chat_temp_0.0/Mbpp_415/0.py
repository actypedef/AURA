"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""
def max_Product(arr):
    # Initialize two variables to store the maximum and second maximum elements
    max1 = float('-inf')
    max2 = float('-inf')
    
    # Iterate through each element in the array
    for i in range(0, len(arr)):
        # Update max1 if the current element is greater than max1
        if arr[i] > max1:
            max2 = max1  # Update max2 to be the previous max1 value
            max1 = arr[i]  # Update max1 to be the current element
        # If the current element is not greater than max1 but is greater than max2
        elif arr[i] > max2:
            max2 = arr[i]  # Update max2 to be the current element
    
    # Return the product of the two largest elements
    return (max1, max2)

# Test the function with the provided test case
assert max_Product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)