"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""
def freq_count(lst):
    # Dictionary to store the frequency of each element
    count_dict = {}
    
    # Iterate through each element in the list
    for item in lst:
        # If the item is already in the dictionary, increment its count
        if item in count_dict:
            count_dict[item] += 1
        # If the item is not in the dictionary, add it with a count of 1
        else:
            count_dict[item] = 1
    
    return count_dict

# Test the function with the provided test case
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]) == {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
