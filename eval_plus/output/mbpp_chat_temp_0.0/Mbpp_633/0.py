"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_Sum(arr, n):
    # Initialize result
    res = 0
    
    # Iterate over each bit position from 0 to 31 (assuming 32-bit integers)
    for i in range(32):
        # Count how many numbers have the i-th bit set
        count = 0
        for j in range(n):
            if arr[j] & (1 << i):
                count += 1
        
        # Calculate the contribution of the i-th bit to the final result
        res += ((count * (n - count)) << i)
    
    return res

# Test the function with the provided test case
assert pair_xor_Sum([5, 9, 7, 6], 4) == 47