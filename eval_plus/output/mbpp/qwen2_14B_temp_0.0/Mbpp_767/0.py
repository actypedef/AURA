"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""
def get_pairs_count(arr, sum):
    # Initialize count variable
    count = 0
    
    # Get the length of the array
    n = len(arr)
    
    # Iterate through each element in the array
    for i in range(n):
        # Iterate through the rest of the elements in the array
        for j in range(i + 1, n):
            # Check if the sum of the pair is equal to the given sum
            if arr[i] + arr[j] == sum:
                count += 1
    
    return count

# Test the function with the provided test case
assert get_pairs_count([1, 1, 1, 1], 2) == 6
