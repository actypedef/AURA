"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
def find_sum(lst):
    # Create a dictionary to store the frequency of each element
    s = dict()
    for i in lst:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
    
    # Calculate the sum of elements that appear only once
    sum = 0
    for key, value in s.items():
        if value == 1:
            sum += key
    
    return sum

# Test the function with the provided test case
assert find_sum([1, 2, 3, 1, 1, 4, 5, 6]) == 21
