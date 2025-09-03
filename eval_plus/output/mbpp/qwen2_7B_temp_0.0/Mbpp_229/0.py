"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""
def re_arrange_array(arr, n):
    # Initialize two pointers, one for the left side and one for the right side
    i = 0
    j = n - 1
    
    while i < j:
        # Move the left pointer until it finds a negative number
        while arr[i] < 0:
            i += 1
        
        # Move the right pointer until it finds a positive number
        while arr[j] >= 0:
            j -= 1
        
        # Swap the elements at the left and right pointers if they are out of place
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    return arr

# Test the function with the provided test case
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]