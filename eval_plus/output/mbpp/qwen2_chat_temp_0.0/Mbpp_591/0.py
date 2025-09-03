"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""
def swap_List(list):
    # Store the first element in a temporary variable
    temp = list[0]
    # Assign the last element to the first position
    list[0] = list[-1]
    # Assign the value stored in the temporary variable to the last position
    list[-1] = temp
    return list

# Test the function with the provided test case
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]