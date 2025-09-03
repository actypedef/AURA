"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, x):
    # Initialize left pointer to 0
    l = 0
    
    # Initialize right pointer to the length of the array minus 1
    r = len(arr) - 1
    
    # Initialize result variable to -1 (indicating not found)
    res = -1
    
    # Perform binary search
    while l <= r:
        mid = l + (r - l) // 2
        
        # If the middle element is greater than x, move the right pointer to mid-1
        if arr[mid] > x:
            r = mid - 1
        
        # If the middle element is less than x, move the left pointer to mid+1
        elif arr[mid] < x:
            l = mid + 1
        
        # If the middle element is equal to x, update result and move the left pointer to mid+1
        else:
            res = mid
            l = mid + 1
    
    # Return the last found index or -1 if not found
    return res

# Test the function with the provided test case
assert last([1, 2, 3], 1) == 0