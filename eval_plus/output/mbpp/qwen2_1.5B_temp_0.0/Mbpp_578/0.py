"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""
def interleave_lists(list1, list2, list3):
    """
    Interleaves three lists of the same length into a single flat list.

    Args:
    list1 (list): The first list.
    list2 (list): The second list.
    list3 (list): The third list.

    Returns:
    list: A single flat list containing elements from all three input lists interleaved.
    """
    # Ensure all lists have the same length
    if len(list1) != len(list2) or len(list2) != len(list3):
        raise ValueError("All input lists must be of the same length.")

    # Interleave the lists using zip and extend
    result = []
    for item1, item2, item3 in zip(list1, list2, list3):
        result.extend([item1, item2, item3])

    return result

# Test the function with provided data points
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]