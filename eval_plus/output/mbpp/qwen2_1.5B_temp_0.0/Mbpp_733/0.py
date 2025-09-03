"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""
def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            # If arr[mid] equals target, move left pointer to the left to find the first occurrence
            right = mid - 1
            
    return left

# Test cases
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
assert find_first_occurrence([1, 3, 4, 4, 4, 5, 7, 8, 9, 9], 4) == 2
assert find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == -1