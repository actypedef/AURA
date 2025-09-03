"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""
def smallest_num(lst):
    # Initialize the minimum number with the first element of the list
    min_num = lst[0]
    
    # Iterate through each number in the list
    for x in lst:
        # Update min_num if a smaller number is found
        if x < min_num:
            min_num = x
    
    return min_num

# Test the function with the provided test case
assert smallest_num([10, 20, 1, 45, 99]) == 1
