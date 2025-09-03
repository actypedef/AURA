"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""
def max_sum_list(lists):
    # Initialize variables to store the maximum sum and the list with this sum
    max_sum = float('-inf')
    max_list = []
    
    # Iterate through each list in the list of lists
    for sublist in lists:
        # Calculate the sum of the current sublist
        current_sum = sum(sublist)
        
        # Check if the current sum is greater than the maximum sum found so far
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = sublist
    
    # Return the sublist with the highest sum
    return max_list

# Test the function with the provided test case
assert max_sum_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [10, 11, 12]