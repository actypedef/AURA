"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""
def get_median(arr1, arr2, n):
    # Initialize pointers for both arrays
    i = 0
    j = 0
    
    # Variable to store the median
    median = 0
    
    # Counter to reach the middle element
    count = 0
    
    # Loop until we reach the middle of the combined array
    while count < n + 1:
        count += 1
        
        # If elements of arr1 are exhausted, take from arr2
        if i == n:
            median = arr2[0]
            break
        elif j == n:
            median = arr1[0]
            break
        
        # Compare elements from both arrays and take the smaller one
        if arr1[i] <= arr2[j]:
            median = arr1[i]
            i += 1
        else:
            median = arr2[j]
            j += 1
    
    # Return the median
    return median

# Test the function with the provided test case
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
