"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
def count_Occurrence(test_tup, test_list):
    # Initialize the result variable to store the count of occurrences
    res = 0
    
    # Iterate through each element in the list
    for ele in test_list:
        # Count occurrences of each element in the tuple and add to the result
        res += test_tup.count(ele)
    
    return res

# Test the function with the provided test case
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3
