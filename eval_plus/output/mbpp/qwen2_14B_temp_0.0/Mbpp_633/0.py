"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_Sum(arr, n):
    res = 0
    # Iterate through each bit position
    for i in range(0, 32):
        cnt = 0
        # Count how many numbers have the i-th bit set
        for j in range(0, n):
            if (arr[j] & (1 << i)):
                cnt += 1
        # Calculate the contribution of the i-th bit to the result
        temp = cnt * (n - cnt) * (1 << i)
        res += temp
    return res

# Test the function with the provided test case
assert pair_xor_Sum([5, 9, 7, 6], 4) == 47