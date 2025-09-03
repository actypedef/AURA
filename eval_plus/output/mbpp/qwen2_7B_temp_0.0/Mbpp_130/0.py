"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""
def max_occurrences(nums):
    # Create a dictionary to store the frequency of each element
    freq = {}
    
    # Iterate through the list and update the frequency count for each element
    for i in nums:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    
    # Initialize variables to track the maximum frequency and its corresponding element
    max_freq = -1
    max_item = -1
    
    # Iterate through the frequency dictionary to find the element with the highest frequency
    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            max_item = key
    
    return max_item

# Test the function with the provided test case
assert max_occurrences([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]) == 2
