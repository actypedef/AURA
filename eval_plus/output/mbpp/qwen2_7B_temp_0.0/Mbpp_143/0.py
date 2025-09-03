"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""
def find_lists(test_tup):
    # Initialize count to zero
    res = 0
    
    # Iterate through each element in the tuple
    for ele in test_tup:
        # Check if the element is an instance of list
        if isinstance(ele, list):
            res += 1
    
    return res

# Test the function with the provided test case
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2