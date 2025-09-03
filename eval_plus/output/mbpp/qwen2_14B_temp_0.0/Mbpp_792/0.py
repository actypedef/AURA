"""
Write a python function to count the number of lists in a given number of lists.
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""
def count_list(input_list):
    # Initialize a counter to keep track of the number of lists
    return len(input_list)

# Test the function with the provided test case
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
