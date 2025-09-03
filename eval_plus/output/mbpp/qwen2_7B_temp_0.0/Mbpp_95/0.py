"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""
def Find_Min_Length(lists):
    # Use the min function along with a generator expression to find the minimum length
    return min(len(lst) for lst in lists)

# Test the function with the provided test case
assert Find_Min_Length([[1], [1, 2]]) == 1
