"""
Write a function to sort the given array by using shell sort.
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""
def shell_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Start with a big gap, then reduce the gap
    gap = n // 2
    
    # Keep reducing the gap until it becomes 0
    while gap > 0:
        # Do a gapped insertion sort for this gap size.
        # The first element in gap sorted array is always at arr[0]. We don't need to visit
        # arr[0] since it is already in its correct place
        for i in range(gap, n):
            temp = arr[i]
            
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp
        
        # Reduce the gap for the next round
        gap //= 2

# Test the function with the provided test case
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
