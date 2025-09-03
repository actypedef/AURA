"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""
def check_greater(arr, n):
    # Iterate through each element in the array
    for i in arr:
        # Check if the current element is greater than or equal to 'n'
        if i >= n:
            return True
    # If no element is found to be greater than 'n', return False
    return False

# Test cases to verify the correctness of the function
assert check_greater([1, 2, 3, 4, 5], 4) == False
