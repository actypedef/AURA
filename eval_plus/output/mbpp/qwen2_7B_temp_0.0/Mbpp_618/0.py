"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(list1, list2):
    # Check if both lists have the same length
    assert len(list1) == len(list2), "Both lists must have the same number of elements"
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate through each pair of elements from the input lists
    for i in range(len(list1)):
        # Calculate the division of corresponding elements and append to the result list
        result.append(float(list1[i]) / float(list2[i]))
    
    return result

# Test the function with the provided test case
assert div_list([4, 5, 6], [1, 2, 3]) == [4.0, 2.5, 2.0]