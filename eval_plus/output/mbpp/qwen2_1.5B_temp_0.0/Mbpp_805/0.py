"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""
def max_sum_list(lst):
    # Initialize variables to store the maximum sum and the corresponding sublist
    max_sum = float('-inf')
    max_sublist = []
    
    # Iterate through each sublist in the given list
    for sublist in lst:
        # Calculate the sum of the current sublist
        current_sum = sum(sublist)
        
        # Update the maximum sum if the current sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
            max_sublist = sublist
    
    return max_sublist

# Test the function with the provided data point
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]) == [10, 11, 12]