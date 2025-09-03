"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""
def right_insertion(arr, x):
    # Initialize the left pointer to 0
    l = 0
    
    # Iterate through the array while the left pointer is less than the length of the array
    while l < len(arr):
        # If the current element is greater than or equal to x, return the current index
        if arr[l] >= x:
            return l
        # Move the left pointer one step to the right
        l += 1
    
    # If no suitable position is found, return the length of the array
    return l

# Test the function with the provided test case
assert right_insertion([1, 2, 4, 5], 6) == 4