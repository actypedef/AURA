"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
from collections import Counter

def frequency_lists(lst):
    # Flatten the list of lists into a single list
    flat_list = [item for sublist in lst for item in sublist]
    
    # Use Counter to count the frequency of each element in the flattened list
    freq_dict = dict(Counter(flat_list))
    
    return freq_dict

# Test the function with the provided test case
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
