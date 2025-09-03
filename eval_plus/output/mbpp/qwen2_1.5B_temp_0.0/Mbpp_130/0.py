"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""
def max_occurrences(lst):
    # Create a dictionary to store the frequency of each element
    freq_dict = {}
    
    # Iterate through the list and update the frequency count
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    
    # Find the item with the maximum frequency
    max_freq_item = max(freq_dict, key=freq_dict.get)
    
    return max_freq_item

# Test the function with the provided test case
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == 2