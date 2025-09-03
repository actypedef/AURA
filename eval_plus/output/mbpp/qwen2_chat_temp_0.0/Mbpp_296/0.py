"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""
def get_Inv_Count(arr):
    # Initialize counter for inversions
    inv_count = 0
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # If an inversion is found, increment the counter
            if arr[i] > arr[j]:
                inv_count += 1
                
    return inv_count

# Test the function with the provided test case
assert get_Inv_Count([1, 20, 6, 4, 5]) == 5