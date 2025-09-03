"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""
def binary_search(arr, low, high, x):
    # Helper function to perform binary search
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    return -1

def is_majority(arr, n, x):
    # Function to check if x is the majority element
    index = binary_search(arr, 0, n - 1, x)
    if index == -1:
        return False
    count = 0
    for i in range(index, n):
        if arr[i] == x:
            count += 1
        else:
            break
    return count > n / 2

# Test the function with the provided test case
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True