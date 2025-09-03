"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""
def max_subarray_product(arr):
    # Initialize variables to store the maximum product so far, minimum product so far,
    # and the current product (which resets at each iteration)
    max_so_far = arr[0]
    min_so_far = arr[0]
    curr_max = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # If the current number is negative, swap the max and min values
        if arr[i] < 0:
            max_so_far, min_so_far = min_so_far, max_so_far

        # Update the current maximum and minimum products
        curr_max = max(arr[i], curr_max * arr[i])
        min_so_far = min(arr[i], min_so_far * arr[i])

        # Update the overall maximum product found so far
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

# Test the function with the provided test case
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112