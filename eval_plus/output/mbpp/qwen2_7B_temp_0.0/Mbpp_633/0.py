"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_Sum(arr, n):
    # Initialize result
    res = 0
    
    # Iterate over each element in the array
    for i in range(n):
        # XOR current element with all other elements
        for j in range(i + 1, n):
            res += (arr[i] ^ arr[j])
    
    return res

# Test the function with the provided test case
assert pair_xor_Sum([5, 9, 7, 6], 4) == 47
