"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""
def find_first_occurrence(arr, x):
    # Initialize the left pointer to the start of the array
    l = 0
    
    # Initialize the right pointer to the end of the array
    r = len(arr) - 1
    
    # Loop until the left pointer is less than or equal to the right pointer
    while l <= r:
        mid = (l + r) // 2
        
        # If the middle element is greater than the target value, move the right pointer left
        if arr[mid] > x:
            r = mid - 1
        
        # If the middle element is less than the target value, move the left pointer right
        elif arr[mid] < x:
            l = mid + 1
        
        # If the middle element is equal to the target value, check for the first occurrence
        else:
            if mid == 0 or arr[mid - 1] != x:
                return mid
            else:
                r = mid - 1
    
    # Return -1 if the target value is not found
    return -1

# Test the function with the provided test case
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1