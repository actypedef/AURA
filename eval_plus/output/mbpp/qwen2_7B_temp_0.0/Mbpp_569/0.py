"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""
def sort_sublists(list1):
    # Sort each sublist in the given list of lists
    sorted_list = [sorted(sublist) for sublist in list1]
    return sorted_list

# Test the function with the provided test case
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
