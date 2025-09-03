"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""
def odd_length_sum(arr):
    n = len(arr)
    total_sum = 0
    
    # Iterate over all possible starting points for subarrays
    for i in range(n):
        # Calculate the length of the current subarray
        length = (n - i) // 2
        
        # Add the sum of the current subarray to the total sum
        total_sum += (length * (length + 1) * (2 * length + 1)) // 6
        
    return total_sum

# Test cases
assert odd_length_sum([1,2,4]) == 14
assert odd_length_sum([1,3,5,7]) == 36
assert odd_length_sum([10,20,30,40,50]) == 900