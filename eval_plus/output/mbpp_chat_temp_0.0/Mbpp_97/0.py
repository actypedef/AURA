"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
def frequency_lists(lists):
    # Initialize an empty dictionary to store frequencies
    freq = {}
    
    # Iterate through each sublist in the list of lists
    for sublist in lists:
        # Iterate through each element in the sublist
        for element in sublist:
            # If the element is already in the dictionary, increment its count
            if element in freq:
                freq[element] += 1
            # If the element is not in the dictionary, add it with a count of 1
            else:
                freq[element] = 1
    
    # Return the dictionary containing frequencies of elements
    return freq

# Test the function with the provided test case
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}