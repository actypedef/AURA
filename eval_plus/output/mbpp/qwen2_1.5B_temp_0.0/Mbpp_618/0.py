"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(list1, list2):
    # Check if both lists have the same length
    assert len(list1) == len(list2), "Both lists must have the same length"
    
    # Divide each pair of elements from the two lists
    result = [a / b for a, b in zip(list1, list2)]
    
    return result

# Test cases to verify the correctness of the solution
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
assert div_list([7,8,9],[2,3,4])==[3.5,2.6666666666666665,2.25]
assert div_list([10,11,12],[1,1,1])==[10.0,11.0,12.0]