"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""
def swap_List(newList):
    # Store the first element in a temporary variable
    temp = newList[0]
    
    # Assign the last element to the first position
    newList[0] = newList[-1]
    
    # Assign the value stored in temp (original first element) to the last position
    newList[-1] = temp
    
    return newList

# Test the function with the provided test case
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
