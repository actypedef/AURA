"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""
def odd_length_sum(arr):
    n = len(arr)
    total_sum = 0
    
    # Iterate over all possible starting points of subarrays
    for i in range(n):
        # Calculate the number of subarrays starting at index i
        count = (i + 1) * (n - i)
        
        # If the count is odd, add the sum of elements from index i to total_sum
        if count % 2 != 0:
            total_sum += sum(arr[i:n])
    
    return total_sum

# Test the function with the provided test case
assert odd_length_sum([1, 2, 4]) == 14