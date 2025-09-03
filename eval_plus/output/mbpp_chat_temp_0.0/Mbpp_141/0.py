"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
def flip(arr, i):
    # Reverse the array from 0 to i
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max_index(arr, n):
    # Find the index of the maximum element in arr[0..n-1]
    max_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def pancake_sort(arr):
    # Sorts the given array using the Pancake sorting algorithm
    curr_size = len(arr)
    while curr_size > 1:
        # Find the index of the maximum element in arr[0..curr_size-1]
        mi = find_max_index(arr, curr_size)
        
        # Move the maximum number to end of current array if it's not already at the end
        if mi != curr_size - 1:
            # First move the maximum number to beginning
            flip(arr, mi)
            
            # Now move the maximum number to end by reversing current array
            flip(arr, curr_size - 1)
        curr_size -= 1
    
    return arr

# Test the function with the provided test case
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]