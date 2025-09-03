"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""
def positive_count(arr):
    # Initialize counters for positive and total elements
    pos = 0
    total = len(arr)
    
    # Iterate through each element in the array
    for i in range(total):
        # Check if the current element is greater than or equal to zero
        if arr[i] >= 0:
            pos += 1
    
    # Calculate the ratio of positive elements
    return (pos / total)

# Test the function with the provided test case
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
