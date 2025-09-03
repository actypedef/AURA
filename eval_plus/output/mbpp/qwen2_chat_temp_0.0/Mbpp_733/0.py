"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""
def find_first_occurrence(arr, target):
    # Initialize the left pointer to the start of the array
    left = 0
    
    # Initialize the right pointer to one past the end of the array
    right = len(arr)
    
    # Loop until the pointers meet
    while left < right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the element at mid is less than the target, move the left pointer to mid + 1
        if arr[mid] < target:
            left = mid + 1
        else:
            # Otherwise, move the right pointer to mid
            right = mid
    
    # Return the left pointer as the index of the first occurrence of the target
    return left

# Test the function with the provided test case
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1