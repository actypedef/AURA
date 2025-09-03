"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""
def split_Arr(arr, n):
    # Split the array into two parts at index n
    arr = arr[n:] + arr[:n]
    return arr

# Test the function with the provided test case
assert split_Arr([12, 10, 5, 6, 52, 36], 2) == [5, 6, 52, 36, 12, 10]