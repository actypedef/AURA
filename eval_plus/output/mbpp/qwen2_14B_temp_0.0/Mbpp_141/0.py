"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
def pancake_sort(arr):
    def flip(sub_arr, k):
        # Reverse the sub-array from the start to the k-th element
        start = 0
        while start < k:
            sub_arr[start], sub_arr[k] = sub_arr[k], sub_arr[start]
            start += 1
            k -= 1

    n = len(arr)
    for i in range(n):
        # Find the index of the maximum element in the unsorted portion of the array
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # Move the maximum element to the end of the unsorted portion
        if max_index != i:
            # Flip the maximum element to the front if it's not already there
            flip(arr, max_index)
            # Flip it to its correct position
            flip(arr, i)

    return arr

# Test the function with the provided test case
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
