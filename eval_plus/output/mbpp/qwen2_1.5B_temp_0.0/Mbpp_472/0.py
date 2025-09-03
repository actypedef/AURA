"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""
def check_Consecutive(lst):
    # Check if the length of the list is less than 2
    if len(lst) < 2:
        return False
    
    # Iterate through the list starting from the second element
    for i in range(1, len(lst)):
        # If the current element is not equal to the previous element plus one
        if lst[i] != lst[i-1] + 1:
            return False
    
    # If all elements are consecutive, return True
    return True

# Test cases
assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,3,4,5]) == False
assert check_Consecutive([1,2,3,4,5,6]) == True
assert check_Consecutive([1,2,3,4,5,7]) == False
assert check_Consecutive([1,2,3,4,5,6,7]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,1