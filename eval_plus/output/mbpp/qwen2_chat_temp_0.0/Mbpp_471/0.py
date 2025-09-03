"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""
def find_remainder(arr, n):
    # Initialize result as 1
    res = 1
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Update result by multiplying it with the current element modulo n
        res = (res * arr[i]) % n
    
    # Return the final result modulo n
    return res

# Test the function with the provided test case
assert find_remainder([100, 10, 5, 25, 35, 14], 11) == 9