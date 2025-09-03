"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
def sum_Of_Subarray_Prod(arr):
    # Initialize the result variable to store the sum of products
    res = 0
    
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Calculate the product of the current element with all elements before it
        prod = arr[i]
        for j in range(i - 1, -1, -1):
            prod *= arr[j]
        
        # Add the product to the result
        res += prod
    
    return res

# Test the function with the provided test case
assert sum_Of_Subarray_Prod([1, 2, 3]) == 20