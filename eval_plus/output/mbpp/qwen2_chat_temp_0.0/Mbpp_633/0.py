"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_Sum(arr, n):
    # Initialize result
    res = 0
    
    # Iterate over each bit position (0 to 31 for 32-bit integers)
    for i in range(32):
        count_ones = 0
        count_zeros = 0
        
        # Count number of ones and zeros at the current bit position
        for j in range(n):
            if arr[j] & (1 << i):
                count_ones += 1
            else:
                count_zeros += 1
        
        # Calculate contribution of current bit to the final result
        res += (count_ones * count_zeros * (1 << i))
    
    return res

# Test the function with the provided test case
assert pair_xor_Sum([5, 9, 7, 6], 4) == 47