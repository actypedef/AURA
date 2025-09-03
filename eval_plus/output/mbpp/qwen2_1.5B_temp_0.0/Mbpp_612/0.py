"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""
def merge(list_of_lists):
    # Initialize two empty lists to store the merged results
    result = []
    
    # Iterate over each sublist in the input list
    for sublist in list_of_lists:
        # Append the first element of the current sublist to the first list in the result
        result[0].append(sublist[0])
        
        # Append the second element of the current sublist to the second list in the result
        result[1].append(sublist[1])
    
    return result

# Test the function with the provided test case
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]