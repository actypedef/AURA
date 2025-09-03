"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""
def is_Monotonic(A):
    # Check if the array is sorted in non-decreasing order
    x = all(A[i] <= A[i + 1] for i in range(len(A) - 1))
    # Check if the array is sorted in non-increasing order
    y = all(A[i] >= A[i + 1] for i in range(len(A) - 1))
    
    # Return True if either condition is met, indicating the array is monotonic
    return x or y

# Test the function with the provided test case
assert is_Monotonic([6, 5, 4, 4]) == True
