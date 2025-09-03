"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
def heap_sort(arr):
    # Convert list into a heap
    heapq.heapify(arr)
    
    # Extract elements from the heap one by one
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    
    return sorted_arr

# Test the function with the provided test case
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
