"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""
def frequency(num_list, n):
    # Count the occurrences of n in num_list
    return num_list.count(n)

# Test the function with the provided test case
assert frequency([1, 2, 3], 4) == 0
