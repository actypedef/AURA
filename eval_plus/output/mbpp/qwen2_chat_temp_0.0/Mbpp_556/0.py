"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
def find_Odd_Pair(arr, n):
    # Initialize result variable
    res = 0
    
    # Iterate through all elements in the array
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # Check if XOR of current pair is odd
            if ((arr[i] ^ arr[j]) & 1):
                res += 1
                
    return res

# Test the function with the provided test case
assert find_Odd_Pair([5, 4, 7, 2, 1], 5) == 6