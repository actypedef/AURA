"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""
def check_min_heap(arr):
    # Check if the given array represents a min heap
    n = len(arr)
    
    # Start from the last non-leaf node and go up to the root
    for i in range(n // 2 - 1, -1, -1):
        # If the current node is greater than its children, it's not a min heap
        if arr[i] > arr[2 * i + 1]:
            return False
        if (2 * i + 2 < n) and (arr[i] > arr[2 * i + 2]):
            return False
    
    # If all conditions are met, it's a min heap
    return True

# Test the function with the provided test case
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
