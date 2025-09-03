"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""
def re_arrange_array(arr, n):
    # Initialize two pointers for the leftmost negative and rightmost positive positions
    i = 0
    j = n - 1
    
    while True:
        # Move the left pointer to the right until a positive number is found
        while i <= j and arr[i] < 0:
            i += 1
        
        # Move the right pointer to the left until a negative number is found
        while i <= j and arr[j] > 0:
            j -= 1
        
        # If the left pointer is less than or equal to the right pointer, swap the elements
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            break
    
    return arr

# Test the function with the provided test case
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]