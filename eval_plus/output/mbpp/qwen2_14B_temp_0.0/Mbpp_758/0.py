"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""
def unique_sublists(list1):
    result = {}
    
    # Iterate through each sublist in the input list
    for l in list1:
        # Convert the sublist to a tuple and use it as a key in the dictionary
        result.setdefault(tuple(l), list()).append(1)
    
    # Sum the occurrences for each tuple key
    for key in result.keys():
        result[key] = sum(result[key])
    
    return result

# Test the function with the provided test case
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]) == {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
