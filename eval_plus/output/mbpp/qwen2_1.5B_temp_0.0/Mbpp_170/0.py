"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""
def sum_range_list(lst, start_index, end_index):
    # Check if the start index is less than or equal to the end index
    if start_index > end_index:
        return "Error: Start index cannot be greater than end index."
    
    # Calculate the sum of numbers in the specified range
    total_sum = sum(lst[start_index:end_index+1])
    
    return total_sum

# Test cases to verify the correctness of the function
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
assert sum_range_list([1,2,3,4,5], 1, 3) == 9
assert sum_range_list([-1, -2, -3, -4, -5], 2, 4) == -6
assert sum_range_list([10, 20, 30, 40, 50], 0, 4) == 150
assert sum_range_list([], 0, 2) == "Error: List is empty."
assert sum_range_list([100], 0, 0) == 100