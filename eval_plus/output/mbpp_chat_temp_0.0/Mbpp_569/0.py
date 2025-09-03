"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""
def sort_sublists(list1):
    # Sort each sublist using the sorted() function and store it back in the original list
    for i in range(len(list1)):
        list1[i] = sorted(list1[i])
    return list1

# Test the function with the provided test case
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
