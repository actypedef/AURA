"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""
def smallest_num(numbers):
    # Initialize the minimum value to be the first element of the list
    min = numbers[0]
    
    # Iterate through each number in the list
    for i in range(1, len(numbers)):
        # Update the minimum value if a smaller number is found
        if numbers[i] < min:
            min = numbers[i]
    
    # Return the smallest number found
    return min

# Test the function with the provided test case
assert smallest_num([10, 20, 1, 45, 99]) == 1
