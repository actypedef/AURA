"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""
def right_insertion(arr, x):
    # Initialize left pointer
    l = 0
    
    # Initialize right pointer
    r = len(arr) - 1
    
    # Loop until the pointers meet or cross each other
    while l <= r:
        mid = (l + r) // 2
        
        # If the middle element is less than x, move the left pointer to mid + 1
        if arr[mid] < x:
            l = mid + 1
            
        # If the middle element is greater than x, move the right pointer to mid - 1
        elif arr[mid] > x:
            r = mid - 1
            
        # If the middle element is equal to x, return mid as the insertion point
        else:
            return mid
    
    # Return the insertion point where x should be placed
    return l

# Test the function with the provided test case
assert right_insertion([1, 2, 4, 5], 6) == 4