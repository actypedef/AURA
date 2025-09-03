"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""
def sort_sublists(list1):
    # Sort each sublist in the list of lists
    result = [sorted(x) for x in list1]
    return result

# Test the function with the provided test case
assert sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
