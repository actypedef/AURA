"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
def comb_sort(arr):
    # Initialize gap size and shrink factor
    gap = len(arr)
    shrink_factor = 1.247
    sorted = False

    # Continue until gap is less than 1 or array is sorted
    while gap > 1 or sorted:
        if gap < 1:
            gap = 1
        gap = int(gap / shrink_factor)

        # Perform a gapped insertion sort
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

    return arr

# Test the function with the provided test case
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
