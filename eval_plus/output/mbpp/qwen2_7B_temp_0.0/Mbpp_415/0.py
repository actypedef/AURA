"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""
def max_Product(arr):
    # Initialize the maximum product to negative infinity
    max_product = float('-inf')
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # Calculate the product of the current pair
            product = arr[i] * arr[j]
            
            # Update the maximum product if the current product is greater
            if product > max_product:
                max_product = product
    
    # Return the pair with the highest product
    return (arr[0], arr[1])

# Test the function with the provided test case
assert max_Product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)
