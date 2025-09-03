"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""
def count_same_pair(list1, list2):
    # Use a generator expression to count indices where the values in both lists are the same
    return sum(1 for i in range(len(list1)) if list1[i] == list2[i])

# Test the function with the provided test case
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9]) == 4
