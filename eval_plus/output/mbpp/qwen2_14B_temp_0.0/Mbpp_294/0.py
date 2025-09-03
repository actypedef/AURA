"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""
def max_val(list1):
    # Initialize max with the first element of the list
    max = list1[0]
    
    # Iterate through each element in the list
    for x in list1:
        # Update max if the current element is greater than max
        if isinstance(x, (int, float)) and x > max:
            max = x
    
    return max

# Test the function with the provided test case
assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
