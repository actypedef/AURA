"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""
def get_pairs_count(arr, target_sum):
    # Initialize counter for pairs
    count = 0
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check all subsequent elements for pair sum
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                count += 1
                
    return count

# Test the function with the provided test case
assert get_pairs_count([1, 1, 1, 1], 2) == 6