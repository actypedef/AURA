"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""
def _sum(arr):
    # Initialize the sum variable to zero
    total = 0
    
    # Iterate through each element in the array
    for x in arr:
        # Add the current element to the total sum
        total += x
    
    # Return the computed sum
    return total

# Test the function with the provided test case
assert _sum([1, 2, 3]) == 6
