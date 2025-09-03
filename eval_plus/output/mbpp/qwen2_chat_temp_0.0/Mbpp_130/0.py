"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""
def max_occurrences(nums):
    # Initialize variables to store the maximum frequency and the corresponding element
    max_frequency = 0
    max_element = None
    
    # Create a dictionary to count occurrences of each element
    freq_dict = {}
    
    # Iterate through the list to populate the dictionary with frequencies
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Iterate through the dictionary to find the element with the maximum frequency
    for key, value in freq_dict.items():
        if value > max_frequency:
            max_frequency = value
            max_element = key
    
    return max_element

# Test the function with the provided test case
assert max_occurrences([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]) == 2