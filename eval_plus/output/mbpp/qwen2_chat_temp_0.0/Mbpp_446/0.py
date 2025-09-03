"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
def count_Occurrence(test_tup, K):
    # Initialize result counter
    res = 0
    
    # Iterate through each element in the tuple
    for ele in test_tup:
        # Check if the element is in the list K
        if ele in K:
            # Increment the result counter
            res += 1
            
    return res

# Test the function with provided data points
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3