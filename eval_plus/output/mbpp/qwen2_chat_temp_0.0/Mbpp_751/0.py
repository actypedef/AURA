"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""
def check_min_heap(arr):
    # Function to check if the given array represents a min heap
    n = len(arr)
    
    # Check each non-leaf node for the min heap property
    for i in range(n // 2 - 1, -1, -1):
        if arr[i] > arr[2 * i + 1]:
            return False
        if (2 * i + 2 < n) and (arr[i] > arr[2 * i + 2]):
            return False
    
    return True

# Test the function with the provided test case
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
