"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""
def check_min_heap(arr):
    # Iterate over each node starting from the second element (index 1)
    for i in range(1, len(arr)):
        # Check if the current node is less than its parent
        if arr[i] < arr[(i - 1) // 2]:
            return False
    return True

# Test the function with the provided test case
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
