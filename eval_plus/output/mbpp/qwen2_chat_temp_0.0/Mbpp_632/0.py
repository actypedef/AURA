"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""
def move_zero(arr):
    # Initialize an index variable to track non-zero elements' position
    i = 0
    
    # Iterate through the array
    for j in range(len(arr)):
        # If the current element is not zero, swap it with the element at the 'i' index
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    return arr

# Test the function with the provided test case
assert move_zero([1, 0, 2, 0, 3, 4]) == [1, 2, 3, 4, 0, 0]