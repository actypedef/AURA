"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""
def unique_sublists(lst):
    # Create an empty dictionary to store the frequency of each sublist
    freq = {}
    
    # Iterate over each sublist in the input list
    for sublist in lst:
        # Convert the sublist to a tuple so it can be used as a dictionary key
        t = tuple(sublist)
        
        # If the tuple is already in the dictionary, increment its count
        if t in freq:
            freq[t] += 1
        # Otherwise, add the tuple to the dictionary with a count of 1
        else:
            freq[t] = 1
    
    # Return the dictionary containing the frequencies of all sublists
    return freq

# Test the function with the provided test case
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]) == {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
