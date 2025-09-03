"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
def comb_sort(arr):
    gap = len(arr)
    shrink_factor = 1.3
    while gap > 1 or any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        gap = int(gap / shrink_factor)
        if gap < 1:
            gap = 1
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]

# Test cases
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]