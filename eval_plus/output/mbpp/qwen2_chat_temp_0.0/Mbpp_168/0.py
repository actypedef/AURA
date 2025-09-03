"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""
def frequency(arr, x):
    # Initialize a counter variable to zero
    count = 0
    
    # Iterate through each element in the array
    for i in arr:
        # If the current element matches the target value, increment the counter
        if i == x:
            count += 1
            
    # Return the total count of occurrences
    return count

# Test the function with the provided test case
assert frequency([1, 2, 3], 4) == 0
