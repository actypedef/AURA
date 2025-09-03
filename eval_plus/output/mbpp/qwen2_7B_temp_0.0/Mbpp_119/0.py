"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""
def search(arr):
    # Initialize left pointer at the start of the array
    l = 0
    
    # Initialize right pointer at the end of the array
    r = len(arr) - 1
    
    # Loop until the pointers meet
    while l < r:
        mid = (l + r) // 2
        
        # Check if the middle element is at an even index and its next element is different
        if mid % 2 == 0 and arr[mid] != arr[mid + 1]:
            return arr[mid]
        
        # Check if the middle element is at an odd index and its previous element is different
        elif mid % 2 == 1 and arr[mid] != arr[mid - 1]:
            return arr[mid]
        
        # Adjust pointers based on the value comparison
        if arr[l] <= arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    
    # Return the last element as the single occurrence
    return arr[r]

# Test the function with the provided test case
assert search([1, 1, 2, 2, 3]) == 3
