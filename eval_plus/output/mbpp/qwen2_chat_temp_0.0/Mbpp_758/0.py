"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""
def unique_sublists(lst):
    # Initialize an empty dictionary to store tuples and their counts
    dict = {}
    
    # Iterate over each sublist in the given list
    for sublist in lst:
        # Convert the sublist to a tuple and check if it already exists in the dictionary
        if tuple(sublist) not in dict:
            # If not, add it with a count of 1
            dict[tuple(sublist)] = 1
        else:
            # If yes, increment the count by 1
            dict[tuple(sublist)] += 1
    
    # Return the dictionary containing tuples and their counts
    return dict

# Test the function with the provided test case
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]) == {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}