"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""
def right_insertion(arr, val):
    # Initialize left and right pointers
    l, r = 0, len(arr) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if arr[mid] < val:
            l = mid + 1
        else:
            r = mid - 1
            
    return l

# Test cases
assert right_insertion([1,2,4,5],6)==4