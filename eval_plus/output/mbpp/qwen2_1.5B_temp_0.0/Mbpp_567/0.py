"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""
def issort_list(lst):
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return True
    
    # Iterate through the list starting from the second element
    for i in range(1, len(lst)):
        # If the current element is less than the previous element, the list is not sorted
        if lst[i] < lst[i-1]:
            return False
    
    # If no elements were found to be out of order, the list is sorted
    return True

# Test cases to verify the correctness of the function
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
assert issort_list([1,3,5,7,9,11,13,15,17,19])==False
assert issort_list([])==True
assert issort_list([10])==True
assert issort_list([1,2,3,4,5,6,7,8,9,10])==True
assert issort_list([10,9,8,7,6,5,4,3,2,1])==False