"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""
def reverse_Array_Upto_K(arr, k):
    # Reverse the array from index 0 to k-1
    arr[:k] = arr[:k][::-1]
    return arr

# Test cases
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
assert reverse_Array_Upto_K([7, 8, 9, 10, 11, 12],3) == [9, 8, 7, 10, 11, 12]
assert reverse_Array_Upto_K([13, 14, 15, 16, 17, 18],5) == [15, 14, 13, 16, 17, 18]