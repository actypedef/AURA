"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""
def check_min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < n and arr[i] > arr[left_child]:
            return False
        if right_child < n and arr[i] > arr[right_child]:
            return False
    return True

# Test cases
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
assert check_min_heap([1, 3, 2, 4, 5, 6]) == False
assert check_min_heap([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
assert check_min_heap([10, 20, 30, 40, 50, 60, 70, 80, 90, 101]) == False