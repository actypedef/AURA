"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""
def re_arrange_array(arr, n):
    # Initialize two pointers for the current position to place negative and positive numbers
    i = 0
    j = 0
    
    # Iterate through the array up to the specified number of elements
    while j < n:
        # If the current element is negative, swap it with the element at index i
        if arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    
    return arr

# Test the function with the provided test case
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]