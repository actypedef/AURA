"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
def sum_of_subarray_prod(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= arr[j]
            total_sum += current_product
    return total_sum

# Test cases
assert sum_of_subarray_prod([1,2,3]) == 20
assert sum_of_subarray_prod([4,5,6]) == 720
assert sum_of_subarray_prod([10,20,30]) == 3600