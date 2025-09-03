"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""
def pack_consecutive_duplicates(lst):
    # Initialize an empty list to store the result
    result = []
    # Iterate through the input list
    for i in range(len(lst)):
        # Append the current element to the result list
        result.append([lst[i]])
        # Check if the next element is the same as the current one
        while i + 1 < len(lst) and lst[i] == lst[i + 1]:
            result[-1].append(lst[i + 1])
            i += 1
    return result

# Test the function with the provided test case
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]