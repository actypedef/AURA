"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""
def get_pairs_count(nums, target_sum):
    # Create a dictionary to store the frequency of each number
    num_freq = {}
    for num in nums:
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1
    
    # Initialize the count of pairs
    pair_count = 0
    
    # Iterate through the numbers in the list
    for num in nums:
        complement = target_sum - num
        if complement in num_freq:
            # If the complement exists in the dictionary, add the product of their frequencies to the pair count
            pair_count += num_freq[complement]
    
    return pair_count

# Test the function with the provided test case
assert get_pairs_count([1,1,1,1],2) == 6
