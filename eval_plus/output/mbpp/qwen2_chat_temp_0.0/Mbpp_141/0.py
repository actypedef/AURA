"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
def flip(arr, i):
    # Reverse elements from 0 to i
    arr[:i+1] = reversed(arr[:i+1])

def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        # Find the index of the maximum element in arr[0..curr_size-1]
        max_index = arr.index(max(arr[:curr_size]))
        
        # Move the maximum number to end of current array if it's not already at the end
        if max_index != curr_size - 1:
            # Bring the maximum number to beginning (by reversing current array)
            flip(arr, max_index)
            
            # Now move the maximum number to end by reversing current array
            flip(arr, curr_size - 1)

# Test the function with the provided test case
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]