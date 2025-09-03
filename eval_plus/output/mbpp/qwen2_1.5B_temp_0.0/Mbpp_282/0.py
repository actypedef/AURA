"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
def sub_list(list1, list2):
    # Check if both lists have the same length
    assert len(list1) == len(list2), "Both lists must have the same length"
    
    # Subtract each pair of elements from the corresponding positions in the lists
    result = [a - b for a, b in zip(list1, list2)]
    
    return result

# Test cases to verify the correctness of the function
assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
assert sub_list([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
assert sub_list([-1, -2, -3], [1, 2, 3]) == [-2, -4, -6]