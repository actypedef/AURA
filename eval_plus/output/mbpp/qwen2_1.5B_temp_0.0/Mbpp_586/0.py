"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""
def split_Arr(arr, n):
    # Split the array into two parts: arr[:n] and arr[n:]
    first_part = arr[:n]
    second_part = arr[n:]
    
    # Add the first part to the end of the second part
    result = second_part + first_part
    
    return result

# Test cases to verify the correctness of the solution
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
assert split_Arr([1,2,3,4,5],3) == [4,5,1,2,3]
assert split_Arr(['a','b','c','d'],1) == ['b', 'c', 'd', 'a']