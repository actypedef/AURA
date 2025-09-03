"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""
def get_pairs_count(arr, target_sum):
    # Initialize a counter for the number of pairs
    count = 0
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Compare the current element with all other elements
        for j in range(i + 1, len(arr)):
            # Check if the sum of the pair equals the target sum
            if arr[i] + arr[j] == target_sum:
                # Increment the counter if condition is met
                count += 1
                
    # Return the total count of pairs
    return count

# Test the function with the provided test case
assert get_pairs_count([1, 1, 1, 1], 2) == 6