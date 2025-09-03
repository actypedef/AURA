"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
def find_sum(nums):
    # Create an empty dictionary to store the frequency of each element
    freq = {}
    
    # Iterate over each number in the input list
    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    
    # Initialize the sum of non-repeated elements
    sum_non_repeated = 0
    
    # Iterate over the frequency dictionary
    for key, value in freq.items():
        # If the frequency of the element is 1, add it to the sum
        if value == 1:
            sum_non_repeated += key
    
    return sum_non_repeated

# Test the function with the provided test case
assert find_sum([1, 2, 3, 1, 1, 4, 5, 6]) == 21
