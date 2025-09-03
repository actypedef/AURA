"""
Write a python function to count the number of lists in a given number of lists.
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""
def count_list(input_list):
    # Initialize a counter for the number of lists
    list_count = 0
    
    # Iterate through each element in the input list
    for i in input_list:
        # Check if the current element is a list
        if isinstance(i, list):
            # Increment the counter if it is a list
            list_count += 1
            
    # Return the total count of lists found
    return list_count

# Test the function with the provided test case
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4