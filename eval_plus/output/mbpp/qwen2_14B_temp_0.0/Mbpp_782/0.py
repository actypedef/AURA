"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""
def odd_length_sum(arr):
    # Calculate the total sum of elements in the array
    total_sum = sum(arr)
    n = len(arr)
    
    # Calculate the sum of all odd length subarrays
    result = (n * (n + 1)) // 2
    
    return result

# Test the function with the provided test case
assert odd_length_sum([1, 2, 4]) == 14