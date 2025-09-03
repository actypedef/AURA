"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""
def find_first_occurrence(arr, x):
    # Initialize the left pointer to the start of the array
    l = 0
    
    # Initialize the right pointer to the end of the array
    r = len(arr) - 1
    
    # Initialize the result variable to store the index of the first occurrence
    res = -1
    
    # Perform binary search
    while l <= r:
        # Calculate the middle index
        mid = (l + r) // 2
        
        # Check if the middle element is equal to the target value
        if arr[mid] == x:
            # Update the result to the current middle index
            res = mid
            
            # Move the right pointer to the left to continue searching for the first occurrence
            r = mid - 1
        elif arr[mid] < x:
            # If the middle element is less than the target, move the left pointer to the right
            l = mid + 1
        else:
            # If the middle element is greater than the target, move the right pointer to the left
            r = mid - 1
    
    # Return the index of the first occurrence or -1 if not found
    return res

# Test the function with the provided test case
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1