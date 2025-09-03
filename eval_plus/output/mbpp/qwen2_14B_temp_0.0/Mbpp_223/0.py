"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""
def is_majority(arr, n, x):
    # Find the first occurrence of x in arr
    first_index = find_first_occurrence(arr, 0, n - 1, x)
    
    # If x is not present in arr, return False
    if first_index == -1:
        return False
    
    # Calculate the index of the last occurrence of x
    last_index = first_index + n // 2
    
    # Check if the last occurrence of x is within the bounds of the array and is equal to x
    return last_index < n and arr[last_index] == x

def find_first_occurrence(arr, low, high, x):
    # Base case: if the range is invalid, return -1
    if high < low:
        return -1
    
    # Calculate the middle index
    mid = low + (high - low) // 2
    
    # Check if the middle element is the first occurrence of x
    if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
        return mid
    
    # If the middle element is greater than x, search in the left half
    if arr[mid] > x:
        return find_first_occurrence(arr, low, mid - 1, x)
    
    # Otherwise, search in the right half
    return find_first_occurrence(arr, mid + 1, high, x)

# Test the function with the provided test case
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True