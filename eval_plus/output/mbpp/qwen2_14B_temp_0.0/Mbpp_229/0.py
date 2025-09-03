"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""
def re_arrange_array(arr, n):
    # Initialize two pointers for negative and positive numbers
    neg_index = 0
    pos_index = 0
    
    # Create a temporary array to store the rearranged elements
    temp_arr = [0] * n
    
    # Iterate through the original array up to the nth element
    for i in range(n):
        if arr[i] < 0:
            # Place negative elements at the beginning of temp_arr
            temp_arr[neg_index] = arr[i]
            neg_index += 1
        else:
            # Place positive elements at the end of temp_arr
            temp_arr[n + pos_index - 1] = arr[i]
            pos_index += 1
    
    # Copy the rearranged elements back to the original array
    for i in range(n):
        arr[i] = temp_arr[i]

# Test the function with the provided test case
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
