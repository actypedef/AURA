"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""
def is_majority(arr, n, x):
    # Find the first occurrence of x in arr
    i = find_first(arr, x)
    
    # If x is not present in arr, return False
    if i == -1:
        return False
    
    # Check if the frequency of x is greater than n/2
    if ((i + n // 2) < n and arr[i + n // 2] == x):
        return True
    else:
        return False

# Helper function to find the first occurrence of x in arr
def find_first(arr, x):
    low, high = 0, len(arr) - 1
    while high >= low:
        mid = (low + high) // 2
        if (mid == 0 or x > arr[mid - 1]) and (arr[mid] == x):
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Test the function with the provided test case
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True