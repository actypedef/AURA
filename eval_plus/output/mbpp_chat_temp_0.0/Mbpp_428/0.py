"""
Write a function to sort the given array by using shell sort.
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""
def shell_sort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2
    
    # Do a gapped insertion sort for this gap size.
    # The first gap elements arr[0..gap-1] are already in gapped order
    # keep adding one more element until the entire array is gap sorted
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            
            # shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # put temp (the original arr[i]) in its correct location
            arr[j] = temp
        
        gap //= 2

# Test the function with the provided test case
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]