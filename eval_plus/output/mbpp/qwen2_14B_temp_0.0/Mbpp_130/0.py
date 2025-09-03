"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""
from collections import defaultdict

def max_occurrences(nums):
    # Dictionary to store the frequency of each number
    frequency = defaultdict(int)
    
    # Update the frequency of each number in the list
    for num in nums:
        frequency[num] += 1
    
    # Find the number with the maximum frequency
    result = max(frequency, key=frequency.get)
    
    return result

# Test the function with the provided test case
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == 2
