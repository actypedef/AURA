"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
def pancake_sort(arr):
    n = len(arr)
    while n > 1:
        # Find the index of the maximum element in arr[0..n-1]
        max_index = arr.index(max(arr[:n]))
        
        # Move the maximum element to the end of the array
        if max_index != n - 1:
            arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[n - 1:] = arr[n - 1:][:max_index + 1][::-1]
        
        # Decrease the size of the unsorted portion
        n -= 1

# Test the function
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]