"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
def comb_sort(arr):
    # Initialize gap size and shrink factor
    gap = len(arr)
    shrink_factor = 1.3
    sorted = False
    
    while not sorted or gap > 1:
        # Calculate next gap value
        if gap > 1:
            gap = int(gap / shrink_factor)
        
        # Set sorted flag to True
        sorted = True
        
        # Perform comparisons and swaps
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False

# Test the function with the provided test case
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
