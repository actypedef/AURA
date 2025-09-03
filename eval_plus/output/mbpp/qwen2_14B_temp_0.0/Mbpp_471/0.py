"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""
def find_remainder(arr, n):
    # Initialize mod to 1
    mod = 1
    
    # Iterate through each element in the array
    for num in arr:
        # Update mod with the product modulo n
        mod = (mod * num) % n
    
    return mod

# Test the function with the provided test case
assert find_remainder([100, 10, 5, 25, 35, 14], 11) == 9
