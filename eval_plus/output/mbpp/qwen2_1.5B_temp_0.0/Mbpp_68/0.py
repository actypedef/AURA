"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""
def is_Monotonic(arr):
    # Check if the array is non-decreasing
    increasing = all(x <= y for x, y in zip(arr, arr[1:]))
    
    # Check if the array is non-increasing
    decreasing = all(x >= y for x, y in zip(arr, arr[1:]))
    
    # Return True if either condition is true, otherwise return False
    return increasing or decreasing

# Test cases
assert is_Monotonic([6, 5, 4, 4]) == True
assert is_Monotonic([1, 2, 3, 4, 5]) == True
assert is_Monotonic([1, 3, 2, 4, 5]) == False
assert is_Monotonic([10, 9, 8, 7, 6]) == True
assert is_Monotonic([10, 9, 8, 7, 8]) == False