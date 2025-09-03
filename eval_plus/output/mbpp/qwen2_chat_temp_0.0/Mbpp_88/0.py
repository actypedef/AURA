"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""
def freq_count(nums):
    # Initialize an empty dictionary to store frequencies
    freq = {}
    
    # Iterate over each number in the list
    for num in nums:
        # If the number is already in the dictionary, increment its count
        if num in freq:
            freq[num] += 1
        # Otherwise, add the number to the dictionary with a count of 1
        else:
            freq[num] = 1
    
    # Return the dictionary containing element frequencies
    return freq

# Test the function with the provided test case
assert freq_count([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]) == {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
