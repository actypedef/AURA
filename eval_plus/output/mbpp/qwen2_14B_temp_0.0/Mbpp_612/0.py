"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""
def merge(list1):
    # Initialize two empty lists to store the separated elements
    result = [[], []]
    
    # Iterate over each sublist in the input list
    for l in list1:
        # Append the first element of the sublist to the first list in result
        result[0].append(l[0])
        # Append the second element of the sublist to the second list in result
        result[1].append(l[1])
    
    return result

# Test the function with the provided test case
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
