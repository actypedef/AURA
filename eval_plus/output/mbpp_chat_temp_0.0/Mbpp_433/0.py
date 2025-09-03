"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""
def check_greater(arr, x):
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if the current element is less than or equal to x
        if arr[i] <= x:
            return True
    # If no element is found that is less than or equal to x, return False
    return False

# Test the function with the provided test case
assert check_greater([1, 2, 3, 4, 5], 4) == False
