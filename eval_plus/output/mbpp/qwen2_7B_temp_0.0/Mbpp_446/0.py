"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
def count_Occurrence(test_tup, K):
    # Initialize result dictionary to store counts
    res = {}
    
    # Iterate over each element in the tuple
    for ele in test_tup:
        # Check if the element is in the list K
        if ele in K:
            # If the element is already in the dictionary, increment its count
            if ele in res:
                res[ele] += 1
            else:
                # Otherwise, add the element to the dictionary with count 1
                res[ele] = 1
    
    # Return the total count of occurrences
    return sum(res.values())

# Test the function with the provided test case
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3