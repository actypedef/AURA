"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""
def binary_search(arr, low, high, x):
    # Base case: if the search range is invalid
    if high < low:
        return -1
    
    mid = (low + high) // 2
    
    # Check if the middle element is the target and it's the majority element
    if mid > 0 and arr[mid] == x and arr[mid - 1] != x:
        return mid
    elif mid == 0 and arr[mid] == x:
        return mid
    # If the target is greater than the middle element, search in the right half
    elif arr[mid] < x:
        return binary_search(arr, mid + 1, high, x)
    # Otherwise, search in the left half
    else:
        return binary_search(arr, low, mid - 1, x)

def is_majority(arr, n, x):
    # Find the index of the first occurrence of x using binary search
    i = binary_search(arr, 0, n - 1, x)
    
    # If x is not found, return False
    if i == -1:
        return False
    
    # Calculate the last possible index where x can be the majority element
    last_occurrence = i + n // 2
    
    # Check if the last occurrence is within bounds and is equal to x
    if last_occurrence < n and arr[last_occurrence] == x:
        return True
    
    return False

# Test the function with the provided test case
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True