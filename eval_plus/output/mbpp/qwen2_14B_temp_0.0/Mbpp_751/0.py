"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""
def check_min_heap(arr):
    # Iterate through the array up to the last non-leaf node
    for i in range((len(arr) - 2) // 2 + 1):
        # Check if the current node is greater than its left child
        if arr[i] > arr[2 * i + 1]:
            return False
        # Check if the current node is greater than its right child if it exists
        if 2 * i + 2 < len(arr) and arr[i] > arr[2 * i + 2]:
            return False
    return True

# Test the function with the provided test case
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True