"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""
def max_product(arr):
    # Initialize the result variable to store the maximum product
    res = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is greater than the previous one
        if arr[i] > arr[i - 1]:
            # Multiply the result by the current element
            res *= arr[i]
    
    return res

# Test the function with the provided test case
assert max_product([3, 100, 4, 5, 150, 6]) == 3000