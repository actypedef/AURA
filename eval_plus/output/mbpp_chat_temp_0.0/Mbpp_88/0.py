"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""
def freq_count(test_list):
    # Initialize an empty dictionary to store element frequencies
    res = {}
    
    # Iterate over each element in the test list
    for ele in test_list:
        # If the element is already in the dictionary, increment its count
        if ele in res:
            res[ele] += 1
        # Otherwise, add the element to the dictionary with a count of 1
        else:
            res[ele] = 1
    
    # Return the dictionary containing element frequencies
    return res

# Test the function with the provided test case
assert freq_count([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]) == {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}