"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            if mid == len(arr) - 1 or arr[mid + 1] != x:
                return mid
            low = mid + 1
    return -1

# Test cases
assert last([1,2,3],1) == 0
assert last([4,5,6,7,8,9,10],10) == 9
assert last([1,2,3,4,5,6,7,8,9,10],11) == -1
assert last([],1) == -1
assert last([1,1,1,1,1,1,1,1,1,1],1) == 9