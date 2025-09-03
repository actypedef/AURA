"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""
import heapq

def heap_queue_largest(nums, n):
    """
    Write a function to find the n largest integers from a given list of numbers, returned in descending order.
    """
    return heapq.nlargest(n, nums)

# Test cases
assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
assert heap_queue_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == [10, 9, 8, 7, 6]
assert heap_queue_largest([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 2) == [100, 90]
assert heap_queue_largest([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 1) == [1000]
assert heap_queue_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert heap_queue_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == []
assert heap_queue_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert heap_queue_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1) == []
assert heap_queue_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert heap_queue_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -100) == []
assert heap_queue_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1000) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert heap_queue_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1000) == []
assert heap_queue_largest([1, 2, 3, 4, 