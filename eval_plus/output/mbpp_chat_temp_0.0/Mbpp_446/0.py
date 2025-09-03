"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
def count_Occurrence(test_tup, K):
    # Initialize result dictionary
    res = dict()
    
    # Iterate over each element in the tuple
    for ele in test_tup:
        # If the element is in the list K, increment its count in the result dictionary
        if ele in K:
            res[ele] = res.get(ele, 0) + 1
    
    # Return the total count of elements found in K
    return sum(res.values())

# Test the function with the provided test case
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3