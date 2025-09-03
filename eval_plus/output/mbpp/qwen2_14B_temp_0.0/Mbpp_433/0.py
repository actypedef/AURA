"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""
def check_greater(arr, n):
    # Iterate through each element in the array
    for i in range(0, len(arr)):
        # Check if the current element is greater than or equal to n
        if arr[i] >= n:
            return False
    return True

# Test the function with the provided test case
assert check_greater([1, 2, 3, 4, 5], 4) == False