"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(arr, x):
    # Initialize the lower bound index
    low = 0
    
    # Initialize the upper bound index
    high = len(arr) - 1
    
    # Loop until the lower bound index exceeds the upper bound index
    while low <= high:
        mid = (low + high) // 2
        
        # If the middle element is less than or equal to the target value
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid - 1
    
    # Return the left insertion point
    return low

# Test the function with the provided test case
assert left_insertion([1, 2, 4, 5], 6) == 4