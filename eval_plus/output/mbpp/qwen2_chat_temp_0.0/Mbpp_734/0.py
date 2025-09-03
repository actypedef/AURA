"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total_sum = 0
    
    # Iterate over each element in the array
    for i in range(n):
        product = arr[i]
        total_sum += product
        
        # Calculate the sum of products of subarrays ending at index i
        for j in range(i + 1, n):
            product *= arr[j]
            total_sum += product
    
    return total_sum

# Test the function with the provided test case
assert sum_Of_Subarray_Prod([1, 2, 3]) == 20