"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_Sum(nums, n):
    # Initialize the result variable
    res = 0
    
    # Iterate over each number in the list
    for i in range(n):
        # Iterate over each number after the current one
        for j in range(i+1, n):
            # Add the XOR of the two numbers to the result
            res += nums[i] ^ nums[j]
    
    return res

# Test the function with the provided test case
assert pair_xor_Sum([5,9,7,6],4) == 47