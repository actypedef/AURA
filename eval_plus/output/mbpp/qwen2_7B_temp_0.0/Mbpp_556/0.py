"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
def find_Odd_Pair(arr, n):
    # Initialize counter for odd XOR pairs
    odd_xor_pairs = 0
    
    # Iterate over all possible pairs
    for i in range(n):
        for j in range(i + 1, n):
            # Check if XOR of current pair is odd
            if (arr[i] ^ arr[j]) % 2 != 0:
                odd_xor_pairs += 1
                
    return odd_xor_pairs

# Test the function with the provided test case
assert find_Odd_Pair([5, 4, 7, 2, 1], 5) == 6
