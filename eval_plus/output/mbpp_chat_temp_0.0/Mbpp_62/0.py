"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""
def smallest_num(list):
    # Initialize the smallest number as the first element of the list
    small = list[0]
    
    # Iterate through each number in the list
    for x in list:
        # Update the smallest number if the current number is smaller
        if x < small:
            small = x
    
    # Return the smallest number found
    return small

# Test the function with the provided test case
assert smallest_num([10, 20, 1, 45, 99]) == 1
