"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""
def odd_position(lst):
    # Iterate over the list using range starting from 0 and incrementing by 2 (odd indices)
    for i in range(0, len(lst), 2):
        # Check if the number at the current index is even
        if lst[i] % 2 == 0:
            return False
    return True

# Test cases to verify the correctness of the function
assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([2,3,5,7,9,11,13,15]) == True
assert odd_position([2,4,6,8,10,12,14,16]) == False
assert odd_position([1,3,5,7,9,11,13,15]) == True
assert odd_position([2,2,2,2,2,2,2,2]) == True
assert odd_position([1,3,5,7,9,11,13,15,17]) == True
assert odd_position([2,2,2,2,2,2,2,2,2]) == True
assert odd_position([1,3,5,7,9,11,13,15,17,19]) == True
assert odd_position([2,2,2,2,2,2,2,2,2,2]) == True
assert odd_position([1,3,5,7,9,11,13,15,17,19,21]) == True
assert odd_position([2,2,2,2,2,2,2,2,2,2,2]) == True
assert odd_position([1,3,5,7,9,11,13,15,17,19,21,23]) == True
assert odd_position([2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert odd_position([1,3,5,7,9,11,13,15,17,19,21,23,25]) == True
assert odd_position([2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert odd_position([1,3,5,7,9,11,13,15,17,19,21,23,25,27]) == True
assert odd_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert odd_position([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]) == True
assert odd_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert odd_position([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]) == True
assert odd_position([2,2,2,2,2,2,2,2,2,2,2