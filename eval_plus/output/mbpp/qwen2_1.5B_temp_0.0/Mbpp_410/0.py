"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""
def min_val(heterogeneous_list):
    # Initialize the minimum value as the first element of the list
    min_value = heterogeneous_list[0]
    
    # Iterate through each element in the list
    for item in heterogeneous_list:
        # Update the minimum value if the current item is smaller
        if item < min_value:
            min_value = item
    
    return min_value

# Test cases to verify the correctness of the solution
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
assert min_val([10, -2, 7, 8, 9]) == -2
assert min_val(['apple', 'banana', 'cherry']) == 'apple'
assert min_val([True, False, True, True]) == False
assert min_val([1.5, 2.3, 0.1, 3.7]) == 0.1