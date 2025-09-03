"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""
def is_Monotonic(A):
    # Check if the array is non-decreasing or non-increasing
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or 
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

# Test the function with the provided test case
assert is_Monotonic([6, 5, 4, 4]) == True
