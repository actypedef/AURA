"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""
def frequency(lst, num):
    return lst.count(num)

# Test cases
assert frequency([1,2,3], 4) == 0
assert frequency([1,2,3,4,5,6,7,8,9,10], 5) == 1
assert frequency([1,2,3,4,5,6,7,8,9,10], 10) == 1
assert frequency([1,2,3,4,5,6,7,8,9,10], 11) == 0
assert frequency([], 1) == 0
assert frequency([1,1,1,1,1], 1) == 5