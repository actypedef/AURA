"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""
def check_greater(arr, num):
    # Iterate through each element in the array
    for i in arr:
        # Check if the current element is greater than the input number
        if i > num:
            return True
    # If no element is greater than the input number, return False
    return False

# Test cases to verify the correctness of the function
assert check_greater([1, 2, 3, 4, 5], 4) == False
assert check_greater([10, 20, 30, 40, 50], 25) == True
assert check_greater([-1, -2, -3, -4, -5], -6) == True
assert check_greater([0, 0, 0, 0, 0], 0) == True
assert check_greater([100, 200, 300, 400, 500], 100) == True