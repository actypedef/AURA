"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""
def right_insertion(arr, x):
    # Initialize left pointer to 0
    l = 0
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # If current element is less than or equal to x, move left pointer to next position
        if arr[i] <= x:
            l += 1
    
    # Return the final position of the left pointer
    return l

# Test the function with the provided test case
assert right_insertion([1, 2, 4, 5], 6) == 4