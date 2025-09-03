"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""
import heapq

def heap_queue_largest(nums, k):
    # Use heapq.nlargest to get the k largest elements in descending order
    return heapq.nlargest(k, nums)

# Test the function with provided data points
assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3) == [85, 75, 65]