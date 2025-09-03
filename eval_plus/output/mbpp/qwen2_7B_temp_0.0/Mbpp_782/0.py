"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""
def odd_length_sum(arr):
    # Initialize the total sum to zero
    total = 0
    
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Calculate the number of subarrays that include arr[i]
        count = ((i + 1) * (len(arr) - i)) // 2
        
        # If the count is odd, add arr[i] multiplied by the count to the total sum
        if count % 2 != 0:
            total += arr[i] * count
    
    return total

# Test the function with the provided test case
assert odd_length_sum([1, 2, 4]) == 14
