"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
from collections import defaultdict

def frequency_lists(list1):
    # Initialize a defaultdict to store the frequency of each element
    result = defaultdict(int)
    
    # Iterate over each sublist in the list of lists
    for ls in list1:
        # Iterate over each element in the sublist
        for element in ls:
            # Increment the frequency of the element in the result dictionary
            result[element] += 1
    
    return result

# Test the function with the provided test case
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
