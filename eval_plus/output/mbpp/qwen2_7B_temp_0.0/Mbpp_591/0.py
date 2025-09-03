"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""
def swap_List(newList):
    # Store the first element of the list
    temp = newList[0]
    
    # Replace the first element with the last element
    newList[0] = newList[-1]
    
    # Replace the last element with the stored first element
    newList[-1] = temp
    
    return newList

# Test the function with the provided test case
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
