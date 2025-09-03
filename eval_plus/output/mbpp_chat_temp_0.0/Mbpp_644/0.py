"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""
def reverse_Array_Upto_K(arr, k):
    # Reverse elements from index 0 to k-1
    arr[:k] = reversed(arr[:k])
    return arr

# Test the function with the provided test case
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]