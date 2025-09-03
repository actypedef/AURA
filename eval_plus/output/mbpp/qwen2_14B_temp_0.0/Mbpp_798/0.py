"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""
def _sum(arr):
    # Initialize sum to zero
    sum = 0
    
    # Iterate through each element in the array
    for i in arr:
        sum = sum + i
    
    # Return the total sum
    return(sum)

# Test the function with the provided test case
assert _sum([1, 2, 3]) == 6
