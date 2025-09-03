"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""
def odd_length_sum(arr):
    # Initialize the total sum to zero
    total = 0
    
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Calculate the number of subarrays where arr[i] is included
        total += ((i + 1) * (len(arr) - i) + 1) // 2 * arr[i]
    
    return total

# Test the function with the provided test case
assert odd_length_sum([1, 2, 4]) == 14