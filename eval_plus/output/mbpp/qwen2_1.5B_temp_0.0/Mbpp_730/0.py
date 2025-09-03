"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
def consecutive_duplicates(lst):
    # Initialize an empty list to store the result
    result = []
    # Iterate through each element in the input list
    for i in range(len(lst)):
        # If the current element is not equal to the previous one,
        # append it to the result list
        if i == 0 or lst[i] != lst[i-1]:
            result.append(lst[i])
    return result

# Test the function with the provided test case
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]