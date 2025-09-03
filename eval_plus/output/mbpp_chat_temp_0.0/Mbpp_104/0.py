"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""
def sort_sublists(test_list):
    # Sort each sublist using list comprehension and sorted() function
    res = [sorted(sublist) for sublist in test_list]
    return res

# Test the function with the provided test case
assert sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
