"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""
def freq_count(lst):
    # Create an empty dictionary to store frequencies
    freq_dict = {}
    
    # Iterate over each element in the list
    for num in lst:
        # If the number is already in the dictionary, increment its count
        if num in freq_dict:
            freq_dict[num] += 1
        # Otherwise, add the number to the dictionary with a count of 1
        else:
            freq_dict[num] = 1
    
    return freq_dict

# Test the function with the provided data point
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]) == ({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})