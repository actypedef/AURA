"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""
def merge(list1):
    # Initialize two empty lists to store the first and second elements from each sublist
    list2 = []
    list3 = []
    
    # Iterate over each sublist in the input list
    for i in range(len(list1)):
        # Append the first element of the current sublist to list2
        list2.append(list1[i][0])
        # Append the second element of the current sublist to list3
        list3.append(list1[i][1])
    
    # Return a list containing list2 and list3
    return [list2, list3]

# Test the function with the provided test case
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
