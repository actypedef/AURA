"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""
def merge(test_list):
    # Initialize an empty list to store the result
    res = []
    # Iterate over each sublist in the test_list
    for sub in test_list:
        # Append the first element of each sublist to the first list in res
        res[0].append(sub[0])
        # Append the second element of each sublist to the second list in res
        res[1].append(sub[1])

    return res

# Test the function with the provided test case
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
