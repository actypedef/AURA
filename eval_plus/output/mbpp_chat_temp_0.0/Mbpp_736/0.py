"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(arr, x):
    # Initialize the low index to 0
    low = 0
    
    # Iterate through the array while low is less than or equal to high
    while low <= len(arr) - 1:
        mid = (low + len(arr)) // 2
        
        # If the middle element is greater than x, move the high index to mid - 1
        if arr[mid] > x:
            high = mid - 1
        else:
            # Otherwise, move the low index to mid + 1
            low = mid + 1
    
    # Return the final low index as the left insertion point
    return low

# Test the function with the provided test case
assert left_insertion([1, 2, 4, 5], 6) == 4