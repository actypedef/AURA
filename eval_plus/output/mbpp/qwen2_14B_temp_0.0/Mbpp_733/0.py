"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""
def find_first_occurrence(arr, x):
    # Initialize the start and end indices for binary search
    start = 0
    end = len(arr) - 1
    
    # Loop until the start index is less than or equal to the end index
    while start <= end:
        # Calculate the middle index
        mid = (start + end) // 2
        
        # Check if the middle element is the target and is the first occurrence
        if arr[mid] == x and (mid == 0 or arr[mid - 1] != x):
            return mid
        # If the middle element is less than the target, search in the right half
        elif arr[mid] < x:
            start = mid + 1
        # Otherwise, search in the left half
        else:
            end = mid - 1
    
    # Return -1 if the target is not found
    return -1

# Test the function with the provided test case
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
