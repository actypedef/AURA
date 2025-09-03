"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""
def frequency(list1, x):
    # Initialize a counter to zero
    freq = 0
    
    # Iterate through each element in the list
    for i in list1:
        # If the current element matches the target value, increment the counter
        if (i == x):
            freq += 1
            
    # Return the total count of occurrences
    return freq

# Test the function with the provided test case
assert frequency([1, 2, 3], 4) == 0
