"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""
def Find_Min(lst):
    # Use the min function with key=len to find the sublist with the minimum length
    return min(lst, key=len)

# Test the function with the provided test case
assert Find_Min([[1], [1, 2], [1, 2, 3]]) == [1]
