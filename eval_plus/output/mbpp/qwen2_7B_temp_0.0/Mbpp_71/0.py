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
        # Update gap size for next iteration
        gap = int(gap / shrink_factor)

        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(arr):
            # Swap if elements are out of order
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

    return arr

# Test the function with the provided test case
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]