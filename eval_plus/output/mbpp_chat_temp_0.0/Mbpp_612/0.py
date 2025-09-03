"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""
def merge(test_list):
    # Initialize two empty lists to store the results
    res1 = []
    res2 = []
    
    # Iterate through each sublist in the input list
    for sub in test_list:
        # Append the first element of the sublist to res1
        res1.append(sub[0])
        # Append the second element of the sublist to res2
        res2.append(sub[1])
    
    # Return a list containing both result lists
    return [res1, res2]

# Test the function with the provided test case
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
