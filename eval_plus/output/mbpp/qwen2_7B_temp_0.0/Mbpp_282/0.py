"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
def sub_list(A, B):
    # Use list comprehension to subtract elements of B from A
    return [A[i] - B[i] for i in range(len(A))]

# Test the function with the provided test case
assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
