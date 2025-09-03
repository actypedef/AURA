"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
def flip(arr, i):
    # Reverse elements between start and end
    start = 0
    end = i
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        # Find index of maximum element in arr[0..curr_size-1]
        mi = arr.index(max(arr[:curr_size]))
        
        # Move the maximum element to end of current array if it is not already at the end
        if mi != curr_size - 1:
            # First move the maximum number to beginning
            flip(arr, mi)
            
            # Now move the maximum number to its final position
            flip(arr, curr_size - 1)

# Test the function with the provided test case
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
