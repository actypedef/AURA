"""
Write a function to compute the n-th power of each number in a list.
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
def nth_nums(nums, n):
    # Compute the n-th power of each number in the list
    return [num ** n for num in nums]

# Test the function with provided data points
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]