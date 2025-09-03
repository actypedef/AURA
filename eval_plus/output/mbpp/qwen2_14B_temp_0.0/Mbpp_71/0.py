"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
def comb_sort(arr):
    def get_next_gap(gap):
        # Shrink gap by shrink factor
        gap = gap // 1.3
        if gap < 1:
            return 1
        return gap

    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        # Compare all elements with current gap
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                # Swap if elements are not in order
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr

# Test the function with the provided test case
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]