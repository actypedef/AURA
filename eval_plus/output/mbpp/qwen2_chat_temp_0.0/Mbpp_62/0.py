"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""
def smallest_num(list):
    # Initialize the first element as the minimum value
    min = list[0]
    
    # Iterate through each element in the list
    for x in list:
        # Update the minimum value if a smaller element is found
        if x < min:
            min = x
    
    # Return the smallest value found
    return min

# Test the function with the provided test case
assert smallest_num([10, 20, 1, 45, 99]) == 1
