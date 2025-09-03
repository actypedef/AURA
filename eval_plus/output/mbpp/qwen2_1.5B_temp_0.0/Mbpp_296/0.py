"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""
def get_Inv_Count(arr):
    # Initialize inversion count to zero
    inv_count = 0
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # For each element, iterate through all elements after it
        for j in range(i+1, len(arr)):
            # If the current element is greater than any element after it,
            # increment the inversion count
            if arr[i] > arr[j]:
                inv_count += 1
                
    return inv_count

# Test the function with the provided test case
assert get_Inv_Count([1,20,6,4,5]) == 5