"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""
def is_Monotonic(arr):
    """
    Check whether the given array is monotonic or not.
    """
    return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or
            all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))

# Test cases
assert is_Monotonic([6, 5, 4, 4]) == True
assert is_Monotonic([1, 2, 3, 4]) == True
assert is_Monotonic([1, 1, 1, 1]) == True
assert is_Monotonic([1, 2, 3, 2]) == False
assert is_Monotonic([4, 3, 2, 1]) == True
assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
assert is_Monotonic([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
assert is_Monotonic([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == True
assert is_Monotonic([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,