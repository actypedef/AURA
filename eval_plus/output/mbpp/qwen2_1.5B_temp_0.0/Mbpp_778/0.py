"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""
def pack_consecutive_duplicates(lst):
    result = []
    current_sublist = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            if current_sublist:
                result.append(current_sublist)
            current_sublist = [lst[i]]
        else:
            current_sublist.append(lst[i])
    if current_sublist:  # Add the last sublist if it's not empty
        result.append(current_sublist)
    return result

# Test cases
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]