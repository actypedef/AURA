"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
def sum_Of_Subarray_Prod(arr):
    # Initialize the result variable to store the sum of products
    res = 0
    
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Calculate the number of subarrays where arr[i] is included
        left = i + 1
        right = len(arr) - i
        
        # Add the product of arr[i], its count of left subarrays, and right subarrays to the result
        res += arr[i] * left * right
    
    # Return the total sum of products
    return res

# Test the function with the provided test case
assert sum_Of_Subarray_Prod([1, 2, 3]) == 20