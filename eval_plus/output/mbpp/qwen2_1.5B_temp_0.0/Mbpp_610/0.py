"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(lst, k):
    # Check if k is within the valid range
    if k < 0 or k >= len(lst):
        raise ValueError("k must be between 0 and the length of the list minus one")
    
    # Remove the k-th element from the list
    return lst[:k] + lst[k+1:]

# Test cases to verify the correctness of the function
assert remove_kth_element([1,1,2,3,4,4,5,1],3) == [1, 1, 3, 4, 4, 5, 1]
assert remove_kth_element(['a','b','c','d'],2) == ['a', 'b', 'd']
assert remove_kth_element([True,False,True],1) == [True, True]