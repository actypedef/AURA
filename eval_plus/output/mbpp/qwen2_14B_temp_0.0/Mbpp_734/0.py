"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
import itertools

def sum_Of_Subarray_Prod(arr):
    # Generate all possible subarrays using itertools.combinations
    subarrays = [arr[i:j] for i in range(len(arr)) for j in range(i + 1, len(arr) + 1)]
    
    # Calculate the product of each subarray and sum them up
    return sum([1] + [prod(subarray) for subarray in subarrays])

# Helper function to calculate the product of elements in a list
def prod(val):
    ans = 1
    for ele in val:
        ans *= ele
    return ans

# Test the function with the provided test case
assert sum_Of_Subarray_Prod([1, 2, 3]) == 20
