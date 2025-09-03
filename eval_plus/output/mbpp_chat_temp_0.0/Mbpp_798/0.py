"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""
def _sum(arr):
    # Initialize sum to zero
    total = 0
    
    # Iterate through each element in the array
    for i in arr:
        total += i  # Add current element to total sum
    
    return total  # Return the computed sum

# Test the function with the provided test case
assert _sum([1, 2, 3]) == 6
